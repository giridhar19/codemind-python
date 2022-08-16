n=int(input())
l=list(map(int,input().split()))
sum=0
a=set(l)
for i in a:
    if i%2!=0:
        sum=sum+i
print(sum)
