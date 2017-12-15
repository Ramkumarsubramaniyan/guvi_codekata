n=int(raw_input("Enter the number"))
temp=abs(n)
count=0
while(temp!=0):
  temp=int(temp/10)
  #print(temp)
  count=count+1
print (count)

