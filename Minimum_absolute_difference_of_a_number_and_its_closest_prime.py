x=int(input())
d=x
c=0
for i in range(1,x+1):
    if x%i==0:
        c+=1
if c==2:
    print("0")
else:
    for i in range(x,0,-1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            min=i
            break
    while True:
        c=0
        for j in range(1,x+1):
            if x%j==0:
                c+=1
        if c==2:
            max=x
            break
        x+=1
    r1=d-min
    r2=max-d
    if r1<r2:
        print(r1)
    else:
        print(r2)
    