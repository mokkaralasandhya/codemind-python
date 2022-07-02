s=input()
sum=0
for i in s:
    if i.isdigit():
        sum+=ord(i)-48
print(sum)