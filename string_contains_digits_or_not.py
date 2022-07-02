a=int(input())
for k in range(a):
    b=input()
    dc=0
    for i in b:
        if i.isdigit():
            dc+=1
    if(dc!=0):
        print("Yes")
    else:
        print("No")