input_text=input("enter a line of text:")
words=input_text.split()
word_counts={}
for word in words:
        
	word=word.lower()
	word_counts[word]=word_counts.get(word,0)+1
print("word counts:")
print(word_counts)
