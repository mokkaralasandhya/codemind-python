n=int(input())
l=[]
p=0
for i in range(n):
    a=int(input())
    c=0;l=[]
    while a:
        l.append(a%10)
        a=a//10
    p=len(l)
    l.sort()
    for i in range(1,p):
        if l[i]-l[i-1]==1:
            c+=1
    if c==p-1:
        print("YES")
    else:
        print("NO")