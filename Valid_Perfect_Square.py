n=int(input())
arr=[]
for i in range(0,n):
    e=int(input())
    arr.append(e)
for i in range(0,n):
    c=0
    for j in range(1,arr[i]):
        if(j*j==arr[i]):
            c+=1
    if c>0:
        print("True")
    else:
        print("False")