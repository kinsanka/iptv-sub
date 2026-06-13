#!/usr/bin/env python3
import urllib.request

SRC = "https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-rtp2httpd.m3u"
DST = "output.m3u"

PREFIX = "https://cctv.speedtest.netynee.top:9999/rtsp"

def main():
    content = urllib.request.urlopen(SRC).read().decode("utf-8", errors="ignore")

    # 两种情况都兼容
    content = content.replace("rtsp://", PREFIX + "/")
    content = content.replace("rtsp:/", PREFIX)

    with open(DST, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
