t=int(input(""))
for i in range(0,t):
    n=int(input())
    l=n
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if(l==s):
        print("True")
    else:
        print("False")