s=input()
a=[]
r=0
m=0
for i in s:
    if i.isdigit():
        a.append(int(i))
a=set(a)
a=sorted(a)
a=a[::-1]
for i in range(len(a)-1,-1,-1):
    if a[i]%2==0:
        m=1
        a[i],a[len(a)-1]=a[len(a)-1],a[i]
        break
for i in a:
    r=r*10+i
if m==0:
    print(-1)
else:
    print(r)