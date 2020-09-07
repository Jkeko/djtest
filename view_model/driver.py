
# -*- coding: gbk -*-
from selenium import webdriver
import requests, time, json, re
from datetime import datetime, timedelta
from time import sleep
# from lxml import etree
import socket
from hashlib import sha1


class Driver(object):
    def driver(self):
        # """获取cookie"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # 开始最大化
        options.add_argument("--test-type")
        options.add_argument("--ignore-certificate-errors")  # 忽略证书错误

        options.add_argument("--disable-popup-blocking")  # 禁用弹出拦截
        options.add_argument("no-sandbox")  # 取消沙盒模式
        options.add_argument("no-default-browser-check")  # 禁止默认浏览器检查
        options.add_argument("about:histograms")
        options.add_argument("about:cache")

        options.add_argument("disable-extensions")  # 禁用扩展
        options.add_argument("disable-glsl-translator")  # 禁用GLSL翻译

        options.add_argument("disable-translate")  # 禁用翻译
        options.add_argument("--disable-gpu")  # 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--hide-scrollbars")  # 隐藏滚动条, 应对一些特殊页面
        options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片, 提升速度

        options.add_argument("start-maximized")
        options.add_argument("--user-data-dir=C:/Users/wangshuguang11/AppData/Local/Google/Chrome/User Data/Profile 6")  # 浏览器路径
        options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片

        # 初始化driver
        dr = webdriver.Chrome(options=options)
    #     sleep(5)
        return dr
    #
    # def run(self):
    #     self.driver()
if __name__ == '__main__':
    Driver().driver()