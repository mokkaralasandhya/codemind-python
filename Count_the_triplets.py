t=int(input())
while(t):
    a=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in arr:
        for j in arr:
            if i!=j:
                if i+j in arr:
                    c+=1
    if(c==0):
        print(-1)
    else:
        print(c//2)
    t-=1