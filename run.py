#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get
@File    ：capture.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午1:40
"""

from util.download import download_m4s
from util.initialization import file_init, input_msg
from util.login import first_login
from util.merge import merge_audio_video
from util.set_options import set_driver
from util.capture import capture_network_requests


def run():
    file_init()
    video_id, cookie_str = input_msg()
    bilibili_url = f"https://www.bilibili.com/video/{video_id}"

    # 设置driver
    driver = set_driver()

    first_login(driver=driver, url=bilibili_url, cookie_str=cookie_str)

    # 捕获网络请求
    _, req_list = capture_network_requests(
        url=bilibili_url,
        duration=5,
        driver=driver,
        save_dir="save",
    )

    # 下载m4s文件
    audio_path = f"output/audio_{video_id}.mp4"
    video_path = f"output/video_{video_id}.mp4"

    for req in req_list:
        if len(req['name']) == 5:
            download_m4s(url=req['url'], output_filename=audio_path)
        else:
            download_m4s(url=req['url'], output_filename=video_path)

    # 合并音视频
    merge_audio_video(
        video_path=video_path,
        audio_path=audio_path,
        output_path=f"output/merge_{video_id}.mp4"
    )

# 使用示例
if __name__ == "__main__":
    run()


