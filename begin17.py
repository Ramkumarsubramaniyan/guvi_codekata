try:
	n=int(input())
	def getsize(num):
		x=1
		while ((num/10)>=1):
			num=num/10
			x+=1
		return x
	size=getsize(n)
	temp=n
	rem=1
	s=0
	while (int(temp)!=0):
		rem=int(temp)%10
		s=s+(rem**size)
		temp/=10
	if (s==n):
		print ("yes")
	else:
		print ("no")
except ValueError:
	print("invalid input")
