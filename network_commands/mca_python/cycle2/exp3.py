input_string=input("enter a string:")
if(len(input_string)>=2):
	new_string=input_string[-1]+input_string[1:-1]+input_string[0]
	print(new_string)
else:
	print("please enter astring with atleast two characters")
