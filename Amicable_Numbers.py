m=int(input())
n=int(input())
sum=0
sum1=0
for i in range(1,m):
    if m%i==0:
        sum=sum+i
for j in range(1,n):
    if n%j==0:
        sum1=sum1+j
if (sum==n and sum1==m):
    print("Amicable")
else:
    print("Not Amicable")