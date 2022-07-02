n,s=map(int,input().split())
for i in range(1,s+1):
    if i%2!=0:
        print("%d x %d = %d"%(n,i,n*i))