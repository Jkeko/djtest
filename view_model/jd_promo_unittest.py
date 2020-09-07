# -*- coding=utf-8 -*-
import traceback

import requests, json
from time import sleep
# from lxml import etree
import configparser
from view_model.driver import Driver
import jsonpath
class Promo():
    def __init__(self):
        global cookies
        self.dr = Driver().driver()
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini',encoding='utf-8')
        self.dr.get("http://wallet-promo.jd.co.th:8080/#")
        self.dr.find_element_by_id("username").send_keys("bjadmin")
        self.dr.find_element_by_id("password").send_keys("xinxibu456")
        self.dr.find_element_by_class_name("formsubmit_btn").click()
        sleep(2)
        c = self.dr.get_cookies()
        cookies = {}
        # 获取cookie中的name和value,转化成requests可以使用的形式
        for cookie in c:
            cookies[cookie['name']] = cookie['value']
        print(u'cookies--', cookies)

#yanzheng
    def send_bonus(self):
        try:
            send_bonus_headers = eval(self.config.get('send_bonus','headers'))
            send_bonus_url = self.config.get('send_bonus','send_bonus_url')
            bonus_data = eval(self.config.get('send_bonus','bonus_data'))
            response=requests.post(url=send_bonus_url,data=json.dumps(bonus_data),headers=send_bonus_headers,cookies=cookies)
            data = response.json()
            value = jsonpath.jsonpath(data,'$.response')
            if value[0] =='true':

                print('发送券 successful,data--'.decode('gb2312'),response.text)
                return response.json()
            else:
                print('发送券 is fail,data--'.decode('gb2312'), response.text)
                return response.json()
        except Exception as e:
            print(e)
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            self.dr.close()
    def send_coupon(self):
        global cookies
        try:
            send_coupon_headers = self.config.get('send_coupon', 'send_coupon_headers')
            send_coupon_url = self.config.get('send_coupon', 'send_coupon_url')
            send_coupon_data = eval(self.config.get('send_coupon', 'send_coupon_data'))
            send_coupon = requests.post(url=send_coupon_url, headers=eval(send_coupon_headers),data=json.dumps(send_coupon_data),cookies=cookies)
            data = send_coupon.json()
            print(data)
        except Exception as e:
            print(e)
            print('traceback.format_exc():\n%s' % traceback.format_exc())
    def serch_bonus(self):
        global cookies
        # offerid = []
        serch_bonus_headers = self.config.get('serch_bonus','serch_bonus_headers')
        serch_bonus_url = self.config.get('serch_bonus','serch_bonus_url')
        try:
            serch = requests.get(url=serch_bonus_url, headers=eval(serch_bonus_headers), cookies=cookies)
            data = serch.json()
            offerid = []
            print('data',data['rows'])
            for key, value in data['rows'].items():  # 迭代当前的字典层级
                print('value',type(data['rows']))

                #
                # for i in range(0, len(list(value))):
                #     if value[i]['approvalStatus'] == 1:
                #         data = value[i]['offerId']
                #         offerid.append(data)
                #         offerid1 = offerid[0]
                #         offer_bonus_headers = self.config.get('offer_bonus', 'offer_bonus_headers')
                #         url = self.config.get('offer_bonus', 'offer_bonus_url')
                #         offer_bonus_url = url + offerid1
                #         print(offer_bonus_url)
                #         offer = requests.get(url=offer_bonus_url, headers=eval(offer_bonus_headers), cookies=cookies)
                #         print(offer.text)
                #     else:
                #         print('没有需要offer的券')
                #         break
        except Exception as e:
            print(e)
            print('traceback.format_exc():\n%s' % traceback.format_exc())
        self.dr.close()

if __name__ == '__main__':
    p = Promo()
    p.send_coupon()
    p.send_bonus()
    # p.serch_bonus()


