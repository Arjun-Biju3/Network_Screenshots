first_name=["Alice","Bob","charlie"]
count_a=0
for name in first_name:
	count_a +=name.lower().count('a')
print("count of a:",count_a)
