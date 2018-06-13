a,b=input().split(' ')
la={}
lb={}
count=0
size=0
if(len(a)!=len(b)):
	print("no")
	count=1
	size=1
else:
	for x in range(len(a)):
		try:
			if not la[a[x]]:
				la[a[x]]=1
			else:
				la[a[x]]+=1
		except KeyError:
			la[a[x]]=1
		try:
			if not lb[b[x]]:
				lb[b[x]]=1
			else:
				lb[b[x]]+=1
		except KeyError:
			lb[b[x]]=1
		if(la[a[x]]!=lb[b[x]]):
			count+=1
if(count==0 and size==0):
	print("yes")
elif(size==0):
	print("no")
