n,x=map(int,input().split())
s=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        if i==j or i==len(m)-1-j:
            s=s+m[i]
print(s)