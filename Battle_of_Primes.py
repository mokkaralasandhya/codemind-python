def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
x=a+b
for i in range(1,10):
    f=x+i
    if prime(f):
        print(i)
        break