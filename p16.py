def prime(a):
	flag=0
	for x in range(1,a+1):
		if((a%x)==0):
			flag=flag+1
	return flag

def res(y,z):
        list=[]
        for x in range(y+1,z):
            	if(prime(x)==2):
            		list.append(x)
        for x in range(len(list)):
                print(list[x])
        if(len(list)==0):
                print("no primes")
           
            		
m,n=[int(x) for x in input().split(",")]
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
	
