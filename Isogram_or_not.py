a=input()
c=wlc=0
l=len(a)
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                c+=1
    if c==0:
        wlc+=1
    else:
        wlc=0
        break
if wlc==0:
    print("False")
else:
    if wlc==l:
        print("True")
    else:
        print("False")