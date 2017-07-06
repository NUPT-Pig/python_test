# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import time
import json
import os
import base64
import urllib
import hashlib
import re
import rsa
import binascii
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib.pyplot as plt


class SinaWeibo(object):
    def __init__(self, email, password):
        self.request_session = requests.session()
        self.get_login_parameter_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.19)&_=1499331628771"
        self.login_url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=1499331868690"
        self.header = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'zh-CN',
            'Accept-Encoding': 'gzip, deflate',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://weibo.com',
            'Referer': 'http://weibo.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
            'Host': 'login.sina.com.cn'
        }
        self.login_data = {
            "entry": "weibo",
            "gateway": "1",
            "from": "",
            "savestate": "0",
            "qrcode_flag": "false",
            "useticket": "1",
            "pagerefer": "",
            "vsnf": "1",
            "su": "",
            "service": "miniblog",
            "servicetime": "",
            "nonce": "",
            "pwencode": "rsa2",
            "rsakv": "",
            "sp": "",
            "sr": "1745*982",
            "encoding": "UTF-8",
            "cdult": "2",
            "domain": "weibo.com",
            "prelt": "60",
            "url": "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
            "returntype": "META"
        }
        self.email = email
        self.password = password

    def get_login_parameter(self):
        response = self.request_session.get(self.get_login_parameter_url, headers=self.header)

        servertime = re.findall('"servertime":(.*?),', response.text)[0]
        pubkey = re.findall('"pubkey":"(.*?)",', response.text)[0]
        rsakv = re.findall('"rsakv":"(.*?)",', response.text)[0]
        nonce = re.findall('"nonce":"(.*?)",', response.text)[0]

        su = base64.encodestring(urllib.quote(self.email))[:-1]

        rsaPubkey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPubkey, 65537)
        message = str(servertime) + '\t' + str(nonce) + '\n' + self.password
        sp = rsa.encrypt(message, key)
        sp = binascii.b2a_hex(sp)

        self.login_data['servertime'] = servertime
        self.login_data['nonce'] = nonce
        self.login_data['rsakv'] = rsakv
        self.login_data['su'] = su
        self.login_data['sp'] = sp

    def login_weibo(self):
        self.get_login_parameter()
        response = self.request_session.post(self.login_url, data=self.login_data, headers=self.header)
        #print response.text
        login_my_page_url = re.findall("location.replace\(\'(.*?)\'\);", response.text)[0]
        response = self.request_session.get(login_my_page_url)
        print response.text

    def fetch_follows(self, uid):
        # 抓取用户的关注列表
        uid = str(uid)  # 好友列表，进其主页会有 http://weibo.com/u/(uid)
        filename = uid + '.txt'
        already_end = False
        page = 1
        follow_compile = re.compile('uid=([0-9]*)&fnick=([^&]*)&sex=([f|m])')
        while not already_end:
            test_url = 'http://weibo.com/' + uid + '/follow' + '?page=' + str(page)
            res = self.request_session.get(test_url)
            follow_list = follow_compile.findall(res.text)
            if len(follow_list) == 0:
                break
            # f = file(filename, 'a+')
            for i in follow_list:
                print i[0], i[1], i[2]  # uid fnick sex
                # f.write('%s %s %s \n' % (i[0], i[1], i[2]))
            # f.close()
            page += 1

    def research_follows(self, uid):
        uid = str(uid)
        filename = uid + '.txt'
        f = file(filename)
        female = 0
        male = 0
        for i in f.readlines():
            if i[-3] == 'f':
                female += 1
            else:
                male += 1
        print female
        print male

        labels = ['female', 'male']
        x = [female, male]
        plt.pie(x, labels=labels, autopct='%3.1f %%')
        plt.title(uid)
        plt.show()


if __name__ == '__main__':
    client = SinaWeibo(email='**', password='**')
    client.login_weibo()
    #client.fetch_follows(1758294853)
    #client.research_follows(1758294853)