a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    s=0
    c=0
    while t!=0:
        r=t%10
        if r!=0:
            if i%r==0:
                c+=1
        s+=1
        t//=10
    if c==s:
        print(i,end=' ')