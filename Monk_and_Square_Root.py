x=int(input())
for i in range(1,x+1):
    a,b=map(int,input().split())
    c=-1
    if a==0 or b==0:
        print('0')
    else:
        for j in range(0,b):
            if(j*j)%b==a:
                c=j
                break
        print(c)