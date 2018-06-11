try:
	n=int(input())
	if(n==0):
		print(1)
	elif(n>=1):
		a=1
		for x in range(1,n+1):
			a=a*x
		print(a)
	else:
		print("Invalid Input")
except ValueError:
	print("Invalid Input")
