n=int(input())
def hap(n):
    s=0
    c=0
    while n>0:
        r=n%10
        c+=1
        s+=r*r
        n//=10
    if c==1:
        if s==1 or s==7:
            return True
        else:
            return False
    else:
        n=s
        return hap(n)
print(hap(n))