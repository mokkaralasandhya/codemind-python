n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
k=0
for i in a:
    if k==2:
        break
    if(i<=m):
        c+=1
    else:
        k+=1
print(c)