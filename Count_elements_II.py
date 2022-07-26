n1,n2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
k=[]
c=0
for i in range(n1):
    if arr1[i] not in arr2 and arr1[i] not in k:
        k.append(arr1[i])
for i in range(n2):
    if arr2[i] not in arr1 and arr2[i] not in k:
        k.append(arr2[i])
print(len(k))
