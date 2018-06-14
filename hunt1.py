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
			for y in range(x+1,len(l)):
				if(l[x]==l[y]):
					a=l[y]
					count=0
					for z in range(len(res)):
						if(res[z]==a):
							count+=1
					if(count==0):
						res.append(a)
		res.pop(0)
		res.sort()
		if not res:
			print("unique")
		else:
			print (" ".join(str(p) for p in res))
except ValueError:
	print("Invalid Input")

