s=input()
c=0
for i in s:
    if i.isdigit():
        continue
    elif i.isalpha():
        continue
    elif i==' ':
        continue
    else:
        c+=1
print(c)       