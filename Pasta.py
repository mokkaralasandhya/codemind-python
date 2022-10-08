n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    if i in a and b.count(i)==1:
        continue
    else:
        print("No")
        break
else:
    print("Yes")