def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
if prime(a)==1:
    flag=0
    while a>0:
        rem=a%10
        if prime(rem)==1:
            flag=1
            a//=10
        else:
            flag=0
            break
    if flag==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        