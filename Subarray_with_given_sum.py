t=int(input())
for d in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    l=0
    for i in range(n):
        s=0
        r=1
        for u in range(n):
            s=0
            s+=a[i]
            if r==n+1:
                break
            for j in range(i+1,r):
                s+=a[j]
            if(s==m):
                l=1
                print(i+1,r)
                break
            r+=1
        if l==1:
            break
    else:
        print(-1)