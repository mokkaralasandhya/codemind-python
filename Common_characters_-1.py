a=input()
a2=""
res=""
for i in a:
    if i.isupper():
        a2+=i.lower()
    else:
        a2+=i
arr=list(a2.split())
for i in arr:
    for j in i:
        f=0
        for k in arr:
            if j in k:
                f=1
            else:
                f=0
                break
        if f==1:
            res+=j
    break
if len(res)==0:
    print(-1)
else:
    print(res)