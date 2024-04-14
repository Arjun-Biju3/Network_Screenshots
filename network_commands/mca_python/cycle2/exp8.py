input_string=input("enter a string:")
if len(input_string)<2:
	print("string is too short")
else:
	first_char=input_string[0]
	modified_string=first_char+''.join('$' if char==first_char else char for char in input_string[1:])
	print("modified string:",modified_string)
