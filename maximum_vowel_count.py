x=input()
x=x+' '
c=0
max=0
a='aeiouAEIOU'
for i in x:
    if i==' ':
        if max<c:
            max=c
        c=0
    if i in a:
        c+=1
print(max)