a=int(input())
b=input()
arr=list(b.split())
mi=100
for i in arr:
    if len(i)<mi:
        mi=len(i)
c=0
for i in arr:
    if len(i)==mi:
        c+=1
print(c)