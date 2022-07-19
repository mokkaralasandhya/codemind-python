x=int(input())
while x!=0:
    sum=0
    r=0
    c=0
    while(x>0):
        r=x%10
        sum+=r
        c+=1
        x=x//10
    if c==1:
        print(sum)
        break
    else:
        x=sum