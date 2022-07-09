a=input()
vow="aeiouAEIOU"
c=0
arr=[]
for i in a:
    if i in vow:
        if i not in arr:
            arr.append(i)
if len(arr)==0:
    print(-1)
else:
    for i in arr:
        print(i,end=" ")