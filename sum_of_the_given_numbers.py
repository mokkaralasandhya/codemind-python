n=int(input())
arr1=[]
arr2=[]
for i in range(0,n):
    a,b=map(int,input().split())
    arr1.append(a)
    arr2.append(b)
for i in range(0,n):
    print(arr1[i]+arr2[i])