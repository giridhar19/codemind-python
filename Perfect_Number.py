n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count=count+i
k=count
if k==n:
    print('True')
else:
    print("False")