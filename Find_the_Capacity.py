l=list(map(int,input().split()))
sum=1
for i in l:
    if i>1:
        sum=sum*i
cd=((2*sum*512)//1024)
print(str(cd)+'KB')