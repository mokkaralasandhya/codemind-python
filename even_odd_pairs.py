n=int(input())
a=list(map(int,input().split()))
e=[]

o=[]
k=[]
for j in range(n):
    if a[j]%2==0:
        e.append(a[j])
    else:
        o.append(a[j])
if len(e)<len(o):
    for i in range(len(e)):
        k.append(e[i])
        k.append(o[i])
    for i in range(len(e),len(o)):
        k.append(o[i])
    if n%2==0:
        print(*k)
    else:
        k.append(0)
        print(*k)
elif len(e)>len(o):
    for i in range(len(o)):
        k.append(e[i])
        k.append(o[i])
    for i in range(len(o),len(e)):
        k.append(e[i])
    if n%2==0:
        print(*k)
    else:
        k.append(0)        
        print(*k)
else:
    for i in range(len(o)):
        k.append(e[i])
        k.append(o[i])
    print(*k)    
    
        
