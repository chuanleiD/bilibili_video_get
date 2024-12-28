#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get 
@File    ：initialization.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午4:27 
"""
import os


def file_init():
    if not os.path.exists("output"):
        os.makedirs("output")

    if not os.path.exists("save"):
        os.makedirs("save")

    if not os.path.exists("data"):
        os.makedirs("data")


def input_msg() -> (str, str):
    while True:
        video_id = input("请输入B站视频ID：")
        if len(video_id) == 12 or len(video_id) == 11:
            break
        else:
            print("输入格式不对，请重试")

    # 登录并设置cookie
    while True:
        print("请先登录B站，然后复制cookie")
        cookie_str = input("请输入你的cookie, 输入p代表跳过此步骤(data下的cookie仍有效)：")
        if len(cookie_str) > 80:
            break
        elif cookie_str == "p":
            if os.path.exists("data/cookies.json"):
                break
        else:
            print("输入格式不对，请重试")

    if cookie_str == "p":
        cookie_str = None
    return video_id, cookie_str


def main():
    print("hello, world")


if __name__ == '__main__':
    main()
