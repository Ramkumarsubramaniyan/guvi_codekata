try:
	n=int(input())
	if(n<=0):
		print("Invalid Input")	
	l=list(map(int,input().split(' ')))
	if(len(l)!=n):
		print("Invalid Input")
	else:
		res=[0]
		for x in range(len(l)):
			if(l[x]==x):
				res.append(l[x])
		res.pop(0)
		res.sort()
		if not res:
			print("-1")
		else:
			print(' '.join(str(p) for p in res))
except ValueError:
	print("Invalid Input")
