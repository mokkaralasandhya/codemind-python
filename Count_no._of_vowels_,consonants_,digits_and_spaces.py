x=input()
a=len(x)
v=0
c=0
d=0
w=0
for i in range(0,a):
    if(x[i]>='0' and x[i]<='9'):
        d+=1
    elif(x[i]==' '):
        w+=1
    elif(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u'):
        v+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)