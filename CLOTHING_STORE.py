n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]==-1:
        continue
    for j in range(i+1,n):
        if a[i]==a[j]:
            c+=1
            a[j]=-1
            break
print(c)