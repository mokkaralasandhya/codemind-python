n=int(input())
a=list(map(int,input().split()))
m=int(input())
k=0
for i in range(n):
    if m==a[i]:
        print(i)
        k=1
        break
if k==0:
    print(-1)