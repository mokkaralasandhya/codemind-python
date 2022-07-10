a=input()
b=input()
f=0
if len(a)==len(b):
    for i in a:
        if i in b or i.upper() in b or i.lower() in b:
            f=1
        else:
            f=0
    if f==1:
        print("True")
    else:
        print("False")
else:
    print("False")