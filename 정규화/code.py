# import re

# f=open("./code.txt","r")

# data=f.read()

# p=re.compile("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}")
# result=p.findall(data)

# key=""
# for i in range(0,len(result)):
# 	key+=result[i][4]

# print(key)

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