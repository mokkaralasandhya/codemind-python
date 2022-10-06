x=input()
x=x+' '
c=0
a='aeiouAEIOU'
for i in x:
    if i==' ':
        print(c,end=' ')
        c=0
    if i in a:
        c+=1
        