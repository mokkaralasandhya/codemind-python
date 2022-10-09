n=int(input())
a=list(map(int,input().split()))
b=int(input())
k=set(a)
k=list(k)
c=0
for i in k:
    if a.count(i)==b:
        c=1
        print(i,end=' ')
if c==0:
    print(-1)