# coding=utf-8
import traceback
import requests, json
from time import sleep
import configparser
from view_model.driver import Driver
import jsonpath
class Promo():
    def __init__(self):
        global cookies
        self.dr = Driver().driver()
        self.config = configparser.ConfigParser()
        #Django调用文件 必须存储在django目录下
        # self.config.read('djtest/config.ini', encoding='utf-8')
        #脚本调用文件，可以在脚本目录下
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
        self.dr.close()
    def send_bonus(self):
        try:
            send_bonus_headers = eval(self.config.get('send_bonus','headers'))
            send_bonus_url = self.config.get('send_bonus','send_bonus_url')
            bonus_data = eval(self.config.get('send_bonus','bonus_data'))
            response = requests.post(url=send_bonus_url, data=json.dumps(bonus_data), headers=send_bonus_headers, cookies=cookies)
            data = response.json()
            value = jsonpath.jsonpath(data,'$.response')
            if value[0] ==True:
                return 'send bonus is success,the response is:-->'+response.text
            else:
                return 'send bonus is failed,the error is:-->'+response.text
        except Exception as e:
            print(e)
        sleep(1)
    def send_coupon(self):
        try:
            send_coupon_headers = eval(self.config.get('send_coupon', 'send_coupon_headers'))
            send_coupon_url = self.config.get('send_coupon', 'send_coupon_url')
            send_coupon_data = eval(self.config.get('send_coupon', 'send_coupon_data'))
            response = requests.post(url=send_coupon_url, data=json.dumps(send_coupon_data), headers=send_coupon_headers, cookies=cookies)
            data = response.json()
            value = jsonpath.jsonpath(data,'$.response')
            if value[0] ==True:
                return 'send coupon is success,the response is:-->'+response.text
            else:
                return 'send coupon is failed,the error is:-->'+response.text
        except Exception as e:
            print(e)
        sleep(1)
    def serch_bonus(self):
        global cookies
        serch_bonus_headers = eval(self.config.get('serch_bonus','serch_bonus_headers'))
        print('serch_bonus_headers',serch_bonus_headers)

        serch_bonus_url = self.config.get('serch_bonus','serch_bonus_url')
        print('serch_bonus_url', serch_bonus_url)
        try:
            serch = requests.get(url=serch_bonus_url, headers=serch_bonus_headers, cookies=cookies)
            data = serch.json()
            print(type(data))
            print('data[rows]',type(data['rows']))
            serdata = data['rows']
            offerid = []
            print('data',serdata)
            # for key, value in data['rows'].items():  # 迭代当前的字典层级
            #     print('value',type(data['rows']))
            #     print('value', data['rows'])
            #     for i in range(0, data['rows']):
            #         if value[i]['approvalStatus'] == 1:
            #             data = value[i]['offerId']
            #             offerid.append(data)
            #             offerid1 = offerid[0]
            #             offer_bonus_headers = self.config.get('offer_bonus', 'offer_bonus_headers')
            #             url = self.config.get('offer_bonus', 'offer_bonus_url')
            #             offer_bonus_url = url + offerid1
            #             print(offer_bonus_url)
            #             offer = requests.get(url=offer_bonus_url, headers=eval(offer_bonus_headers), cookies=cookies)
            #             return '执行结果--》'+offer.text
            #         else:
            #             print('没有需要offer的券')
            #             break

            for i in range(0, len(serdata)):
                print('serdata[i]',serdata[i])
                if serdata[i]['approvalStatus'] == 1:
                    offdata = serdata[i]['offerId']
                    offerid.append(offdata)
                    offerid1 = offerid[0]
                    offer_bonus_headers = self.config.get('offer_bonus', 'offer_bonus_headers')
                    url = self.config.get('offer_bonus', 'offer_bonus_url')
                    offer_bonus_url = url + offerid1
                    print(offer_bonus_url)
                    offer = requests.get(url=str(offer_bonus_url), headers=eval(offer_bonus_headers), cookies=cookies)
                    print(offer.text)
                    return '执行结果--》'+offer.text
                else:
                    print('没有需要offer的券')


        except Exception as e:
            print(e)
            # print('traceback.format_exc():\n%s' % traceback.format_exc())

if __name__ == '__main__':
    p = Promo()
    # p.send_coupon()
    # p.send_bonus()
    p.serch_bonus()


