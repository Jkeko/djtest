
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
        # """��ȡcookie"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # ��ʼ���
        options.add_argument("--test-type")
        options.add_argument("--ignore-certificate-errors")  # ����֤�����

        options.add_argument("--disable-popup-blocking")  # ���õ�������
        options.add_argument("no-sandbox")  # ȡ��ɳ��ģʽ
        options.add_argument("no-default-browser-check")  # ��ֹĬ����������
        options.add_argument("about:histograms")
        options.add_argument("about:cache")

        options.add_argument("disable-extensions")  # ������չ
        options.add_argument("disable-glsl-translator")  # ����GLSL����

        options.add_argument("disable-translate")  # ���÷���
        options.add_argument("--disable-gpu")  # �ȸ��ĵ��ᵽ��Ҫ����������������bug
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--hide-scrollbars")  # ���ع�����, Ӧ��һЩ����ҳ��
        options.add_argument("blink-settings=imagesEnabled=false")  # ������ͼƬ, �����ٶ�

        options.add_argument("start-maximized")
        options.add_argument("--user-data-dir=C:/Users/wangshuguang11/AppData/Local/Google/Chrome/User Data/Profile 6")  # �����·��
        options.add_argument("blink-settings=imagesEnabled=false")  # ������ͼƬ

        # ��ʼ��driver
        dr = webdriver.Chrome(options=options)
    #     sleep(5)
        return dr
    #
    # def run(self):
    #     self.driver()
if __name__ == '__main__':
    Driver().driver()