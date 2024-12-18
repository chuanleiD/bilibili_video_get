#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：strengthenCountry 
@File    ：set_options.py
@Author  ：ChenLiang
@Date    ：2024/11/29 下午3:28 
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_driver() -> webdriver.Chrome:
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_experimental_option('perfLoggingPrefs', {
        'enableNetwork': True,
        'enablePage': False,
    })
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # 初始化WebDriver和NetworkCapture
    driver = webdriver.Chrome(options=chrome_options)

    return driver


