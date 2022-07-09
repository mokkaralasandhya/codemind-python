a=input()
f=0
vo="aeiou"
for i in vo:
    if i in a:
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")