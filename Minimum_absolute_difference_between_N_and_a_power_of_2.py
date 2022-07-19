n=int(input())
i=0
while(True):
    p=2**i
    if n>=p:
        m1=p
    else:
        m2=p
        break
    i+=1
if m2-n>n-m1:
    print(n-m1)
elif m2-n<n-m1:
    print(m2-n)