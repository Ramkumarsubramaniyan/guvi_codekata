try:
	a=input()
	t=a
	if(int(t)):
		n=len(a)
		temp=a
		res=""
		for x in range(0,n):
			res=res+temp[n-x-1]
		print (res)
except ValueError:	
	print("Invalid Input")
