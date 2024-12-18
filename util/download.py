#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get 
@File    ：download.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午3:47 
"""

import requests


def download_m4s(url, output_filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bilibili.com',
        'Range': 'bytes=0-'  # 支持断点续传
    }

    try:
        # 发送请求并获取响应
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # 检查是否请求成功

        # 打开文件并写入内容
        with open(output_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"下载完成：{output_filename}")
        return True

    except Exception as e:
        print(f"下载失败：{str(e)}")
        return False


def main():
    print("hello, world")


if __name__ == '__main__':
    main()
