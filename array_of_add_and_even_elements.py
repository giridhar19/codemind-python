n=int(input())
l=list(map(int,input().split()))
odd=[]
even=[]
L=1
for i in l:
    if i%2!=0:
        odd.append(i)
    else:
        even.append(i)
k=(odd+even)
print(*k)