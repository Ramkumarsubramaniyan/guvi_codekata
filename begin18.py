try:
	n,m=map(int,input().split())
	def getsize(num):
		x=1
		while ((num/10)>=1):
			num=num/10
			x+=1
		return x
	def avag(z):
		size=getsize(z)
		temp=z
		rem=1
		s=0
		while (int(temp)!=0):
			rem=int(temp)%10
			s=s+(rem**size)
			temp/=10
		if (s==z):
			print (s)
	for a in range(n,m+1):
		avag(a)
except ValueError:
	print("invalid input")
