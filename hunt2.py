try:
	n=int(input())
	if(n<=0):
		print("Invalid Input")	
	l=list(map(int,input().split(' ')))
	if(len(l)!=n):
		print("Invalid Input")
	if(min(l)<0):
		print("Invalid Input")
	else:
		a=len(l)
		res=0
		for x in range(a):
			b=max(l)
			res=res+((10**(a-1))*b)
			l.remove(b)
			a-=1
		print(res)
except ValueError:
	print("Invalid Input")
			
