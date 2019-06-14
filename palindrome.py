n=int(input())
temp=n
sum=0
while(n>0):
	a=n%10
	sum=sum*10+a
	n=n//10
if sum==temp:
	print("yes")
else:
	print("no")
