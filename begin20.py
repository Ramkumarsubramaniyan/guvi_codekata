try:
	n=int(input())
	my_list=[]
	for x in range(0,5):
		my_list.append((x+1)*n)
	print(" ".join(str(x) for x in my_list))
except ValueError:
	print("invalid input")
