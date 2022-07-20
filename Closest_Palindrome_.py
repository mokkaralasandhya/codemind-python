x=int(input())
for i in range(x-1,0,-1):
    d=i
    sum=0
    while d>0:
        r=d%10
        sum=sum*10+r
        d//=10
    if i==sum:
        min=sum
        break
a=x
while True:
    d=x+1
    sum=0
    while d>0:
        r=d%10
        sum=sum*10+r
        d//=10
    if(x+1)==sum:
        max=sum
        break
    x+=1
r1=a-min
r2=max-a
if r1<r2:
    print(min)
elif r1==r2:
    print(min,max)
else:
    print(max)