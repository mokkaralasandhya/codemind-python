n=int(input())
sqr=n*n
temp=n
s=0
rev1=0
rev2=0
while temp>0:
    r=temp%10
    s+=1
    temp//=10
while sqr>0:
    r=sqr%10
    if temp==s:
        break
    rev1=(rev1*10)+r
    temp+=1
    sqr//=10
while rev1>0:
    r=rev1%10
    rev2=(rev2*10)+r
    rev1//=10
if rev2==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")