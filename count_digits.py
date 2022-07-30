n=int(input())
a1=list(map(str,input().split()))
for i in range(n):
    s=len(a1[i])
    if int(a1[i])<0:
        s-=1
    print(s,end=' ')