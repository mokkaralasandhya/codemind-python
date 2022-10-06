a,b=map(int,input().split())
#print(a,b)
c=list(map(int,input().split()))
#print(c)
d=0
for i in c:
    if i<0:
        i=i*-1
    i=str(i)
    if len(i)==b:
        d+=1
print(d)