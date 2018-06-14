try:
	n=int(input())
	if(n<=0):
		print("Invalid Input")
	else:
		l=list(map(int,input().split(' ')))
		if(len(l)!=n):
			print("Invalid Input")
		else:
			flag=0
			flag_1=0
			flag_2=0
			pos=0
			for x in range(len(l)):
				count=l.count(l[x])
				if(count==1):
					flag+=1
					pos=x
				elif(count==2):
					flag_1+=1
				elif(count>2):
					flag+=1
					break
			if(flag==1 and flag_1==n-1 and flag_2==0):
				print(l[pos])
			else:
				print("Invalid Input")
except:
	print("Invalid Input")
