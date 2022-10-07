n,m=map(int,input().split())
sa=[0]*m
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        sa[i]+=m[i]
for k in sa:
    print(k,end=' ')