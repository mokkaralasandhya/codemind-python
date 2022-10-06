x=input()
x=x+' '
c=0
k=0
min=99
a='aeiouAEIOU'
for i in x:
    if i==' ':
        if min>c:
            min=c
        c=0
    if i in a:
        c+=1
for i in x:
    if i==' ':
        if min==c:
            k+=1
        c=0
    if i in a:
        c+=1
print(k)