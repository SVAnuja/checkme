n=int(input())
k=int(input())
x=[]
sum=0
for i in range(n):
	num=int(input())
	x.append(num)
for i in range(k+1):
	sum=sum+i
print(sum)
