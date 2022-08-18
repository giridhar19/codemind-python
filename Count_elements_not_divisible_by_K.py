n,m=map(int,input().split())
l=list(map(int,input().split()))
co=0
for i in l:
    if i%m!=0:
        co=co+1
print(co)