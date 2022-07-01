s=input()
bb=0;aa=0;ll=0;oo=0;nn=0
l=[]
for i in s:
    if i=='b':
        bb+=1
    elif i=='a':
        aa+=1
    elif i=='l':
        ll+=1
    elif i=='o':
        oo+=1
    elif i=='n':
        nn+=1
ll=ll//2
oo=oo//2
l.append(bb)
l.append(aa)
l.append(ll)
l.append(oo)
l.append(nn)
p=min(l)
print(p)