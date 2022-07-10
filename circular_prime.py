def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
def rev(a):
    su=0
    while a>0:
        rem=a%10
        su=(su*10)+rem
        a//=10
    return su
a=int(input())
arev=rev(a)
if prime(a)==1:
    if prime(arev)==1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")