n=int(input())
sum=0
for i in range(n):
    if i*i==n:
        sum+=1
if sum==0:
    print("False")
else:
    print("True")