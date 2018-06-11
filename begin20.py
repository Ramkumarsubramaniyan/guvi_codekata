try:
	n=int(input())
	for x in range(1,6):
		print(n*x)
except ValueError:
	print("invalid input")
