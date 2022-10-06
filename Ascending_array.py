n=int(input())
a=list(map(int,input().split()))
b=a[::1]
c=sorted(set(a))
if c==b:
    print('yes')
else:
    print('no')