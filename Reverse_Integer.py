num=int(input())
def reverseNum(n):
    if n>=0:
        return int(str(n)[::-1])
    else:
        return int('-{val}'.format(val=str(n)[1:][::-1]))
print(reverseNum(num))