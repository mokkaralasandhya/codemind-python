a=input()
vo="aeiou"
c=0
for i in vo:
    if i not in a:
        print(i,end=" ")
        c+=1
if(c==0):
    print(0)
