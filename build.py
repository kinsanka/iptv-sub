#!/usr/bin/env python3
from urllib.request import urlopen

TASKS = [
    {
        "src": "https://raw.githubusercontent.com/sggc/SDU-IPTV-PRO/main/SDU-Unicast.m3u",
        "dst": "output-unicast.m3u",
        "replacements": [
            ("rtsp://", "https://cctv.speedtest.netynee.top:9999/rtsp/"),
        ],
    },
    {
        "src": "https://raw.githubusercontent.com/sggc/SDU-IPTV-PRO/main/SDU-Multicast/SDU-Multicast-Jinan.m3u",
        "dst": "output-multicast-jinan.m3u",
        "replacements": [
            ("http://192.168.100.1:5140", "https://cctv.speedtest.netynee.top:9999"),
            ("rtsp://", "https://cctv.speedtest.netynee.top:9999/rtsp/"),
        ],
    },
]

def fetch_text(url: str) -> str:
    with urlopen(url) as resp:
        return resp.read().decode("utf-8", errors="ignore")

def write_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def main():
    for task in TASKS:
        content = fetch_text(task["src"])
        for old, new in task["replacements"]:
            content = content.replace(old, new)
        write_text(task["dst"], content)
        print(f'Generated {task["dst"]}')

if __name__ == "__main__":
    main()
