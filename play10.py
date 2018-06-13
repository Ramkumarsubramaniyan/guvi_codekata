try:
	a,b=input().split(' ')
	count=0
	if(len(a)!=len(b)):
		if(abs(len(a)-len(b))==1):
			for x in range(min(len(a),len(b))):
				if(a[x]!=b[x]):
					count+=1
			count+=1
	else:
		for x in range(len(a)):
			if(a[x]!=b[x]):
				count+=1
	if(count==1):
		print("yes")
	else:
		print("no")
except ValueError:
	print("Invalid Input")
