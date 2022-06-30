t=int(input())
for l in range(t):
    a,b=map(int,input().split())
    c=0
    for i in range(a):
        s=input()
        arr=[]
        for j in s:
            if j=='P' or j=='T':
                arr.append(j)
        for j in range(a):
            if arr[j]=='P':
                for K in range(a):
                    if arr[K]=='T':
                        if abs(j-K)<=b:
                            c+=1
                            arr[K]='0'
                            break
                continue
    print(c)