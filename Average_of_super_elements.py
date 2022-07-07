n=int(input())
arr=list(map(int,input().split()))
k=[]
sum=0
c=0
for i in range(n):
    if arr[i]!=-1:
        c=1
        for j in range(n):
            if arr[i]==arr[j] and i!=j:
                c+=1
                arr[j]=-1
    if arr[i]==c:
        k.append(arr[i])
for i in range(len(k)):
    sum+=k[i]
if(len(k)==0):
    print(-1)
else:
    avg=sum/len(k)
    print("{:.2f}".format(avg))