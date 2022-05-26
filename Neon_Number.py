n=int(input())
n1=n*n
x=[int(a) for a in str(n1)]
sum=0
for i in x:
    sum=sum+i
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")