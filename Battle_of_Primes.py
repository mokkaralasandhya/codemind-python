a=int(input())
b=int(input())
c=a+b
i=c+1
while i>c:
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:
        print(i-c)
        break
    i+=1