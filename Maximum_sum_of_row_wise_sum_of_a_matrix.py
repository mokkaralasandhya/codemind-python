n,m=map(int,input().split())
p=[]
for i in range(n):
    a=list(map(int,input().split()))
    sa=sum(a)
    p.append(sa)
print(max(p))