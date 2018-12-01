import re

f=open("./game2.txt","r",encoding='utf-8')

code=f.read()

pattern=re.compile("[a-c]{1}[0-9]{2}[A-Z]{1}")

result=pattern.findall(code)

key=""

for i in range(0,len(result)):
	key+=result[i][3]

print(key)