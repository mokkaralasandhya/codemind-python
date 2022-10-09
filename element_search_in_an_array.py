a=int(input())
z=list(map(int,input().split()))
x=int(input())
for i in z:
    if i==x:
        print(True)
        break
else:
    print(False)