a=int(raw_input())
temp=a
flag=0
if(a<0):
	print("negative numbers cannot be prime")
elif(a==0):
	print("not a prime")
else:
	for x in xrange(1,a+1):
		if(a%x==0):
			flag=flag+1

          
	if(flag==2):
		print("prime")
	else:
		print("not a prime")
	
	
