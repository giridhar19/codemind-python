n=int(input())
l=list(map(int,input().split()))
odd=list()
even=list()
for i in l:
    if i%2==0:
        odd.append(i)
    else:
        even.append(i)
print(*odd+even)