def word(s):
    s1=""
    for i in s:
        s1+=i.lower()
    return s1
a=input()
b=input()
c=list(a.split())
d=list(b.split())
w1=[]
for i in c:
    if word(i) not in w1:
        w1.append(word(i))
w2=[]
for i in d:
    if word(i) not in w2:
        w2.append(word(i))
co=0
if len(w1)>len(w2):
    for i in w2:
        if i in w1:
            co+=1
elif len(w1)<len(w2):
    for i in w1:
        if i in w2:
            co+=1
else:
    for i in w1:
        if i in w2:
            co+=1
print(co)