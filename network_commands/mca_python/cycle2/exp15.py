words=input("enter a list words separated by spaces:").split()
longest_length=0
for word in words:
	word_length=len(word)
	if word_length>longest_length:
		longest_length=word_length
print("length of longest word:",longest_length)
