try:
	def count_prime(l,r):
		ta=l
		tb=r
		count=0
		for x in range(ta,tb+1):
			t=0
			for y in range(1,x):
				if((x%y)==0):
					t+=1
			if(t==1):
				count+=1
		return count
	a,b=map(int,input().split(' '))
	if(a<b):
		print(count_prime(a,b))
	else:
		print("Invalid Input")
except ValueError:
	print("Invalid Input")
