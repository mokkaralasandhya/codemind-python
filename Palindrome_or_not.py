a=input()
f=0
le=len(a)
for i in range(le):
    if(a[i]==a[le-i-1] or a[i]==a[le-i-1].upper() or a[i]==a[le-i-1].lower()):
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")