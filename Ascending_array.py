n=int(input())
a=list(map(int,input().split()))
b=set(a)
b=sorted(b)
if a==b:
    print("yes")
else:
    print("no")