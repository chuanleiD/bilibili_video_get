#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get 
@File    ：merge.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午3:53 
"""
# import os
#
#
# def merge_audio_video(video_path, audio_path, output_path):
#     try:
#         cmd = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a copy "{output_path}"'
#         os.system(cmd)
#         print(f"合并完成：{output_path}")
#         return True
#     except Exception as e:
#         print(f"合并失败：{str(e)}")
#         return False


import ffmpeg


def merge_audio_video(video_path, audio_path, output_path):
    try:
        print(f"正在合并：{output_path}，请等待")
        # 合并音频和视频
        video = ffmpeg.input(video_path)
        audio = ffmpeg.input(audio_path)

        stream = ffmpeg.output(
            video,
            audio,
            output_path,
            vcodec='copy',  # 直接复制视频流，不重新编码
            acodec='copy'  # 直接复制音频流，不重新编码
        )

        # 运行ffmpeg命令
        ffmpeg.run(stream, overwrite_output=True)
        return True

    except Exception as e:
        print(f"合并失败：{str(e)}")
        return False


def main():
    print("hello, world")


if __name__ == '__main__':
    main()
