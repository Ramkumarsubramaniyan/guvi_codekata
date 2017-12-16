def prime(a):
	flag=0
	for x in xrange(1,a+1):
		if((a%x)==0):
			flag=flag+1
	return flag
def res(m,n):
	list=[]
	for x in xrange(m+1,n):
            	if(prime(x)==2):
            		print x
            		
m,n=[int(x) for x in raw_input().split(",")]
if(m>n):
	res(n,m)
elif(m<n):
	res(m,n)
elif(m<0 and n<0):
	print("no primes")
elif(m<0):
	res(0,n)
elif(n<0):
	res(m,o)
