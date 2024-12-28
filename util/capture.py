#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bilibili_video_get 
@File    ：capture.py
@Author  ：ChenLiang
@Date    ：2024/12/18 下午1:40 
"""

import json
import os.path
from pathlib import Path
from datetime import datetime
from selenium import webdriver


class NetworkCapture:
    def __init__(self, save_dir="save"):
        # 初始化存储请求的列表
        self.requests = []
        # 创建保存目录
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def process_browser_log(self, logs: list) -> list:
        """处理并格式化捕获到的请求日志"""
        log_list = []
        for entry in logs:
            try:
                log = json.loads(entry['message'])['message']
                # 只处理网络请求
                if 'Network.requestWillBeSent' == log['method']:
                    request = log['params']['request']
                    
                    req_name = request['url'].split('/')[-1].split('?')[0].split('-')[-1].split('.')[0]
                    if request['url'].startswith('https://cn-sh-fx') and req_name not in log_list:
                        print("-if-----------")
                        print(request['url'])
                        print("-if-----------")
                        log_list.append(req_name)
                        self.requests.append({
                            'name': req_name,
                            'url': request['url'],
                            # 'method': request['method'],
                            # 'headers': request['headers'],
                        })
            except Exception as e:
                print(f"处理日志时出错: {str(e)}")
        
        print("-log_list-----------")
        print(log_list[-2:])
        print("-self.requests-----------")
        print(self.requests[-2:])
        return self.requests[-2:]


    def save_requests(self, filename=None):
        """将捕获的请求保存到JSON文件"""
        if not filename:
            # 如果没有指定文件名，使用时间戳创建
            filename = f"requests_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        file_path = os.path.join(self.save_dir, filename)

        # 确保保存的是最新数据
        save_data = {
            'capture_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_requests': len(self.requests),
            'requests': self.requests
        }

        # 将数据写入JSON文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(save_data, file, ensure_ascii=False, indent=2)

        print(f"请求数据已保存到: {file_path}")
        return file_path


def capture_network_requests(url: str, driver: webdriver.Chrome, duration=10, save_dir="save", filename=None) -> (str, list):
    """
    捕获指定网站的网络请求并保存到JSON文件

    参数:
        url: 要访问的网站URL
        duration: 捕获持续时间(秒)
        save_dir: 保存文件的目录
        filename: 保存的文件名（可选）
    """
    capture = NetworkCapture(save_dir)

    try:
        print(f"等待 {duration} 秒以捕获请求...")
        import time
        time.sleep(duration)

        # 获取并处理日志
        logs = driver.get_log('performance')

        # 获取视频链接和cookie
        req_list = capture.process_browser_log(logs)

        # 保存请求数据
        saved_file = capture.save_requests(filename)
        print(f"共捕获到 {len(capture.requests)} 个请求")

        # 读取并打印保存的数据
        with open(saved_file, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            print("\n保存的数据预览:")
            print(f"捕获时间: {saved_data['capture_time']}")
            print(f"总请求数: {saved_data['total_requests']}")
            # print("\n前3个请求:")
            # for req in saved_data['requests'][:3]:
            #     print(f"\n时间: {req['timestamp']}")
            #     print(f"URL: {req['url']}")
            #     print(f"方法: {req['method']}")

        return saved_file, req_list

    finally:
        driver.quit()

