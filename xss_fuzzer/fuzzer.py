# import requests
# import urllib

# # url="http://yeali.me:8835/finn.php?mode="
# url="http://yeali.me/index.php?mode="

# f= open('./xss_vectors.txt',mode='r',encoding='utf-8')
# lines=f.readlines()

# for line in lines:
# 	r=requests.get(url,params=line)

# 	# print(r.status_code)

# f.close()

#--------------------------------------------------------------------------

#1. import 라이브러리
from selenium import webdriver
from threading import Thread
from datetime import datetime
import signal,sys,time,base64
from urllib import request
import tornado.ioloop,tornado.web,tornado.options

#2. url

SERVER_PORT=3030
BASE_URL='http://localhost:9999/?a='
PAYLOADS='payload.txt'
DELAY=3

#3. logger

def LOG(data):
	with open('logs.txt','a')as f:
		f.write(data+"\n")

#Marking timestamp
LOG("Fuzzer Started at : "+str(datetime.now()))

#Firefox Driver Configuration

fp=webdriver.FirefoxProfile()
fp.update_preferences()
DRIVER=webdriver.Firefox(firefox_profile=fp)



