a=input()
a=a.lower()
a=set(a)
d=len(a)
for i in a:
    if i==' ':
        print(d-1)
        break
else:
    print(d)
    
#print(a)