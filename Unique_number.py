a=input()
c=f=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==1:
        f=1
    if c!=1:
        f=0
        break
if(f==1):
    print("Unique Number")
else:
    print("Not Unique Number")