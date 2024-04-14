color_names=input("Enter color names separated by commas:")
colors=[color.strip() for color in color_names.split(',')]
if len(colors)>0:
	print("first colour:",colors[0])
	print("last colour:",colors[-1])
else:
	print("no colurs entered")
