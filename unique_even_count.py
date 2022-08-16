n=int(input())
l=list(map(int,input().split()))
count=0
a=set(l)
for i in a:
    if i%2==0:
        count=count+1
print(count)
