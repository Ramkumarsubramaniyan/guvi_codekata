try:
	n=int(input())
	l=list(map(int,input().split(' ')))
	if(len(l)!=n):
		print("Invalid Input")
	else:
		res=[]
		for x in range(len(l)):
			for y in range(x+1,len(l)):
				if(l[x]==l[y]):
					a=l[y]
					count=0
					for z in range(len(res)+1):
						try:
							if(res[z]==a):
								count+=1
							if(count==0):
								res.append(a)
						except IndexError:
							res.append(a)
		res.sort()
		if not res:
			print("unique")
		else:
			print(res)
except ValueError:
	print("Invalid Input")

