"""CLI for protobuf_parser — parse RakNet protobuf messages from PCAP files.

Usage:
    python -m mn2mc.utils.protobuf_parser_cli -p <pcap> -d <proto-dir>
"""

import argparse
import json
import sys

import blackboxprotobuf
from google.protobuf.json_format import MessageToDict

from mn2mc.utils.protobuf_parser import (
    SCAPY_AVAILABLE,
    TSHARK_AVAILABLE,
    build_msgid_to_class_map,
    compile_proto_files,
    extract_udp_payloads_scapy,
    extract_udp_payloads_tshark,
    parse_message_header,
    parse_raknet_messages,
)


def main():
    parser = argparse.ArgumentParser(
        description="解析 PCAP 中 RakNet 协议内的 Protobuf 数据"
    )
    parser.add_argument("-p", "--pcap", required=True, help="PCAP 文件路径")
    parser.add_argument(
        "-d", "--proto-dir", required=True, help="包含所有 .proto 文件的目录"
    )
    parser.add_argument("--tshark", action="store_true", help="强制使用 tshark 解析")
    parser.add_argument("--scapy", action="store_true", help="强制使用 scapy 解析")
    args = parser.parse_args()

    # 1. 编译 proto 文件并加载消息类
    print("正在编译 Proto 文件...")
    message_classes = compile_proto_files(args.proto_dir)
    print(f"共加载 {len(message_classes)} 个消息类")

    # 2. 构建消息 ID 到消息类的映射
    print("构建消息 ID 映射...")
    id_to_class = build_msgid_to_class_map(message_classes)
    print(f"成功映射 {len(id_to_class)} 个消息 ID")

    # 3. 提取 UDP 负载
    if args.tshark:
        if not TSHARK_AVAILABLE:
            print("tshark 不可用，请安装 Wireshark", file=sys.stderr)
            sys.exit(1)
        udp_payloads = extract_udp_payloads_tshark(args.pcap)
    elif args.scapy:
        if not SCAPY_AVAILABLE:
            print("scapy 不可用，请安装 scapy", file=sys.stderr)
            sys.exit(1)
        udp_payloads = extract_udp_payloads_scapy(args.pcap)
    else:
        if TSHARK_AVAILABLE:
            udp_payloads = extract_udp_payloads_tshark(args.pcap)
        elif SCAPY_AVAILABLE:
            print(
                "警告: tshark 未找到，使用 scapy 解析器（可能不准确）", file=sys.stderr
            )
            udp_payloads = extract_udp_payloads_scapy(args.pcap)
        else:
            print("错误: 未找到 tshark 或 scapy，无法解析 PCAP", file=sys.stderr)
            sys.exit(1)

    print(f"从 {args.pcap} 提取到 {len(udp_payloads)} 个 UDP 负载")

    # 4. 解析每个 UDP 负载中的 RakNet 消息，提取用户数据
    all_user_data = []
    for idx, udp_data in enumerate(udp_payloads):
        raknet_msgs = parse_raknet_messages(udp_data)
        if raknet_msgs:
            print(f"UDP 负载 {idx + 1}: 解析出 {len(raknet_msgs)} 条 RakNet 用户消息")
            all_user_data.extend(raknet_msgs)
        else:
            print(f"UDP 负载 {idx + 1}: 未找到用户消息")

    print(f"总共提取 {len(all_user_data)} 条用户消息数据")

    # 5. 解析每条用户消息
    success_count = 0
    fallback_success_count = 0
    for idx, user_data in enumerate(all_user_data):
        parsed = parse_message_header(user_data)
        if parsed is None:
            print(
                f"\n--- 消息 {idx + 1} 无法解析头，原始数据 (前32字节): {user_data[:32].hex()} ---"
            )
            continue

        msg_id, msg_body, direction = parsed
        print(f"\n--- 消息 {idx + 1} (方向: {direction}, ID: {msg_id}) ---")

        if msg_id not in id_to_class:
            print(f"未知消息 ID {msg_id}")
            print(f"原始数据: {msg_body.hex()}")
            try:
                json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
                if json_msg != "{}":
                    print(json_msg)
                    fallback_success_count += 1
            except Exception:
                pass
            continue

        msg_class = id_to_class[msg_id]
        try:
            proto_msg = msg_class()
            print(msg_class)
            proto_msg.ParseFromString(msg_body)
            json_msg = MessageToDict(proto_msg, preserving_proto_field_name=True)
            print(json.dumps(json_msg, indent=2, ensure_ascii=False))
            success_count += 1
        except Exception as e:
            print(f"解析失败: {e}")
            print(f"数据 (前64字节): {msg_body[:64].hex()}")
            try:
                json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
                if json_msg != "{}":
                    print(json_msg)
                    fallback_success_count += 1
            except Exception:
                pass

    print()
    print(f"解析成功消息数: {success_count}")
    print(f"原始解析消息数: {fallback_success_count}")


if __name__ == "__main__":
    main()
