#!/usr/bin/env python3
from urllib.request import urlopen

TASKS = [
    {
        "src": "https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-rtp2httpd.m3u",
        "dst": "output-unicast.m3u",
        "old": "rtsp://",
        "new": "https://cctv.speedtest.netynee.top:9999/rtsp/",
    },
    {
        "src": "https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jinan.m3u",
        "dst": "output-multicast-jinan.m3u",
        "old": "http://192.168.0.1:5140",
        "new": "https://cctv.speedtest.netynee.top:9999",
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
        content = content.replace(task["old"], task["new"])
        write_text(task["dst"], content)
        print(f'Generated {task["dst"]}')

if __name__ == "__main__":
    main()
