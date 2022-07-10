n=int(input())
a=list(map(int,input().split()))
add=0
for i in a:
    if i%2==0:
        add+=i
print(add)