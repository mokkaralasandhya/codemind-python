def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
T=int(input())
for i in range(T):
    n=int(input())
    print(fact(n))