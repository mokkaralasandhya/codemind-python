n=int(input())
a=list(map(int,input().split()))
k=[]
c=0
for i in a:
    if i not in k:
        k.append(i)
        if a.count(i)==i:
            c+=1
print(c)