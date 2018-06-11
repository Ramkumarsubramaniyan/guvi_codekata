try:
	n=int(input())
	if (n>=1):
		for x in range(1,6):
			print(n*x)
	else:
		print("invalid input")
except ValueError:
	print("invalid input")
