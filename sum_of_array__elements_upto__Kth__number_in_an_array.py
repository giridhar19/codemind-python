n=int(input())
l=list(map(int,input().split()))
m=int(input())
sum=0
for i in l:
    if i<=m:
        sum=sum+i
print(sum)