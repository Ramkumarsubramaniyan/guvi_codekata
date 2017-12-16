a=int(raw_input())
temp=a
x=0
while(temp!=0):
	x=x*10+int(temp%10)
	temp=int(temp/10)
if(x==a):
	print("palindrome")
else:
	print("not a palindrome")


