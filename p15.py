def even(a,b):
	if((a%2)==0):
		if(abs(b-a)==1 or abs(b-a)==2):
			print("no even numbers")
		a=a+2
	          
		while(a!=b and a!=(b+1)):
			print(a)
			a=a+2
	else:
		if(abs(b-a)==0 or abs(b-a)==1):
			print("no even numbers")
		a=a+1
		while(a!=b and a!=(b+1)):
			print(a)
			a=a+2



a,b=[int(x) for x in raw_input().split(",")]
if(a<b):
	even(a,b)
			
elif(a>b):
	temp=a
	a=b
	b=temp
	even(a,b)
else:
	even(a,b)

	
