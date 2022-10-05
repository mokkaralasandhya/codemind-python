n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
a=list(a)
b=list(b)
#print(a,b)
c=0
for i in range(len(a)):
    if a[i] in b:
        #print(a[i])
        c+=1
print(c)