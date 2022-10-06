n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(a[i])
c=b[::-1]
a.sort()
if c==a:
    print('yes')
else:
    print('no')