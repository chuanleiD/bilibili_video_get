#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get
@File    ：capture.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午1:40
"""
import subprocess

from util.download import download_m4s
from util.initialization import file_init, input_msg
from util.login import first_login
from util.merge import merge_audio_video
from util.set_options import set_driver
from util.capture import capture_network_requests
import os


def open_output_folder():
    current_path = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_path, "output")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    subprocess.run(['explorer', output_path])


def run1():
    file_init()
    video_id, cookie_str = input_msg()
    bilibili_url = f"https://www.bilibili.com/video/{video_id}"

    # 设置driver
    driver = set_driver()

    first_login(driver=driver, url=bilibili_url, cookie_str=cookie_str)

    # 捕获网络请求
    _, req_list = capture_network_requests(
        url=bilibili_url,
        duration=10,
        driver=driver,
        save_dir="save",
    )

    # 下载m4s文件
    audio_path = f"output/audio_{video_id}.mp4"
    video_path = f"output/video_{video_id}.mp4"
    output_path = f"output/merge_{video_id}.mp4"
    
    print("----download--------------")
    
    count = 0
    for req in req_list: 
        if count == 0:
            download_m4s(url=req['url'], output_filename=video_path)
            count += 1
        else:
            download_m4s(url=req['url'], output_filename=audio_path)

    # 合并音视频
    merge_audio_video(
        video_path=video_path,
        audio_path=audio_path,
        output_path=output_path
    )
    print(f"合并完成：{output_path}")

    open_output_folder()
    

def run2():
    file_init()

    video_path = ["output\\1.mp4", "output\\2.mp4", "output\\merge.mp4"]
    for i in range(0, 2):
        url = input("请输入直链"+str(i+1)+": ")
        download_m4s(url, video_path[i])
            
    # 合并音视频
    merge_audio_video(
        video_path=video_path[0],
        audio_path=video_path[1],
        output_path=video_path[2]
    )
    print(f"合并完成：{video_path[2]}")

    open_output_folder()
    

def run():
    print()
    print()
    p_str = input('默认采取全自动模式，输入p采用手动模式: ')
    if p_str == "p":
        print("采用手动模式")
        run2()
    else:
        print("采用全自动模式")
        run1()

    # 方法1: 使用input()函数
    input('按任意键退出...')


# 使用示例
if __name__ == "__main__":
    run()
