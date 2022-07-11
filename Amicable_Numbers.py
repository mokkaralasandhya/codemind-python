def sod(a):
    su=0
    for i in range(1,a):
        if a%i==0:
            su+=i
    return su
a=int(input())
b=int(input())
if sod(a)==b and sod(b)==a:
    print("Amicable")
else:
    print("Not Amicable")