n=int(input())
t=n
t2=n
s=0
su=0
while t>0:
    r=t%10
    s+=1
    t//=10
while t2>0:
    r=t2%10
    su+=pow(r,s)
    s-=1
    t2//=10
if su==n:
    print("True")
else:
    print("False")