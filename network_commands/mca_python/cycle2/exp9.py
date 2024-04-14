str1="hello"
str2="world"
if len(str1)>=2 and len(str2)>=2:
	str3=str1[0]+str2[1]+str1[2:]+" "+str2[0]+str1[1]+str2[2:]
	print("resulting string:",str3)
else:
	print("length is too small")
