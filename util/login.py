#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project   ：strengthenCountry
@File      ：login.py
@Author    ：ChenLiang
@Date      ：2024/11/29 下午7:46
@Reference ：https://www.cnblogs.com/xkdn/p/17267520.html
"""

import json
import os
import random
import time
from selenium import webdriver
from typing import List, Dict
from selenium.webdriver.support.wait import WebDriverWait


def convert_cookie_string_to_dict(cookie_string):
    """将F12复制的cookie字符串转换为selenium可用的格式"""
    cookie_dict_list = []
    # 分割成单个cookie
    items = cookie_string.split('; ')

    for item in items:
        if '=' in item:
            name, value = item.split('=', 1)
            cookie_dict = {
                'name': name.strip(),
                'value': value.strip(),
                'domain': '.bilibili.com'  # B站的域名
            }
            cookie_dict_list.append(cookie_dict)

    return cookie_dict_list


def save_cookies_to_file(cookies: List[Dict], filename: str = os.path.join('data', 'cookies.json')) -> None:
    """
    将浏览器cookie保存到json文件

    Args:
        cookies: 浏览器cookie列表
        filename: 保存的文件名
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, ensure_ascii=False, indent=4)
        print(f"Cookie已保存到 {filename}")
    except Exception as e:
        print(f"保存Cookie失败: {str(e)}")


def load_cookies_from_file(filename: str = os.path.join('data', 'cookies.json')) -> List[Dict]:
    """
    从json文件读取cookie

    Args:
        filename: cookie文件名
    Returns:
        cookie列表
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())
        print(f"成功读取Cookie从 {filename}")
        return cookies
    except Exception as e:
        print(f"读取Cookie失败: {str(e)}")
        return []


def apply_cookies_to_driver(driver: webdriver.Chrome, cookies: List[Dict]) -> None:
    """
    将cookie应用到浏览器

    Args:
        driver: selenium浏览器实例
        cookies: cookie列表
    """
    try:
        for cookie in cookies:
            cookie_dict = {
                "domain": cookie.get("domain"),
                "expiry": cookie.get("expiry"),
                "httpOnly": cookie.get("httpOnly"),
                "name": cookie.get("name"),
                "path": cookie.get("path"),
                "sameSite": cookie.get("sameSite"),  # 修复这里
                "secure": cookie.get("secure"),
                "value": cookie.get("value")
            }
            # 移除None值的键，避免selenium报错
            cookie_dict = {k: v for k, v in cookie_dict.items() if v is not None}

            try:
                driver.add_cookie(cookie_dict)
            except Exception as e:
                print(f"添加cookie '{cookie.get('name')}' 失败: {str(e)}")
                continue

        print("cookies载入成功...")
        driver.refresh()  # 刷新网页,cookies才成功
        time.sleep(1 + random.uniform(0.1, 0.9))
        print("Cookie已成功应用到浏览器")
    except Exception as e:
        print(f"应用Cookie失败: {str(e)}")


def first_login(driver: webdriver.Chrome, url: str, cookie_str=None) -> None:
    """
    获取cookies保存至本地
    """
    # 打开指定网页
    driver.get(url)
    wait = WebDriverWait(driver, 20)  # 最大等待 20 秒
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    if cookie_str is not None:
        cookie_list = convert_cookie_string_to_dict(cookie_str)
        save_cookies_to_file(cookie_list)

    # 尝试使用cookie登录
    cookies_path = os.path.join('data', 'cookies.json')

    if os.path.exists(cookies_path):
        print("已存在cookie文件, 尝试使用cookie登录")
        cookies = load_cookies_from_file(cookies_path)
        apply_cookies_to_driver(driver, cookies)
        # 清空之前的日志
        # driver.get_log('performance')  # 获取并丢弃之前的日志
    else:
        print("未找到cookie文件, 请手动登录")

    return

