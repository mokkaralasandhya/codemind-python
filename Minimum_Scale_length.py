n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
c=0
for i in range(a[0],1,-1):
    c=0
    for j in range(n):
        if a[j]%i==0:
            c+=1
    if c==n:
        print(i)
        break
else:
    print('1')