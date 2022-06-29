n=int(input())
s=0
arr=[]
for i in range(n):
    e=int(input())
    arr.append(e)
k=int(input())
for i in range(n):
    if arr[i]<=k:
        s+=1
    if arr[i]>k:
        s+=2
print(s)