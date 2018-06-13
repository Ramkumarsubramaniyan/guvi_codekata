def snake_to_camel(word):
        return ' '.join(x.capitalize() for x in word.split(' '))
try:
	str=input()
	if not str:
		print("Invalid Input")
	else:
		print(snake_to_camel(str))
except ValueError:
	print("Invalid Input")
