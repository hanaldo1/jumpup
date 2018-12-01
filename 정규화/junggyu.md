해당 사이트에 들어가 보니 엄청난 긴 문자열과 함께 `대문자 3개로 둘러싸인 소문자 1개`를 찾으라는 글이 있었다. 

이 문제는 `정규표현식`을 사용하면 쉽게 풀리는 문제였다.

----------------------------------

#### 정규 표현식
사전적 의미 : 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어

* 문자열의 검색과 치환을 위한 용도

#### 메타 문자
: 정규 표현식에는 다양한 메타 문자가 존재한다.
 
*  `.` : 모든 문자와 일치 
* `[특정문자1 - 특정문자2]` : 특정문자 1,2 사이의 모든 문자 중 하나
* `[^x]` : x를 제외한 문자 중 하나
* `^x` : x로 시작하는 문자열
* `x$` : x로 끝나는 문자열
* `x*` : x가 0번 이상 반복
* `x+` : x가 1번 이상 반복
* `x{n}` : x가 n번 반복한 문자

등등 정말 여러 표현들이 있다.   
(추후 모두 정리 예정....)

-------------------------------

해당 문제는 대문자 3개로 둘러싸인 소문자 1개를 찾는 문제였다.

즉, 정규표현식을 사용하면 다음과 같다.

```
[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}
```

전체 코드는 다음과 같다.

```
import re
code = open("./code.txt", 'r')
print("open code")
data = code.read()

p = re.compile("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}")
result = p.findall(data)

print ("search result")

key = ""

for i in range(0, len(result)):
	key += result[i][4]


print (key)
```

key는 다음과 같았다.
```
equisite
```

> key : equisite

-------------------------------------------------

### site : yeali.me/game2

이번에는 소문자 1개와 숫자 2개가 앞에 붙은 대문자 하나를 찾는 문제였다.  
이 또한, 정규표현식을 사용하여 풀면 간단했다.

정규표현식은 다음과 같다.

```
[a-c]{1}[0-9]{2}[A-Z]{1}
```

전체 코드는 다음과 같다.

```
import re

f=open("./game2.txt","r",encoding='utf-8')

code=f.read()

pattern=re.compile("[a-c]{1}[0-9]{2}[A-Z]{1}")

result=pattern.findall(code)

key=""

for i in range(0,len(result)):
	key+=result[i][3]

print(key)
```

key는 다음과 같다.

```
IRREPKAVEABLE
```

>key : IRREPKAVEABLE
