n=input()
s=n.upper()
c2=0
c1=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90)or ord(i)==32:
        c1+=1
    else:
        c2+=1
print(c2)