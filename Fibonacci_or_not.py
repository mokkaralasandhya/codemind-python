n=int(input())
a=0
b=0
c=1
if n==0 or n==1:
    print("True")
while(a<n):
    a=b+c
    b=c
    c=a
if a==n:
    print("True")
else:
    print("False")