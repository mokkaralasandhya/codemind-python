n=input()
s=n.split()
l=len(s)
for i in range(l):
    if i%2==0:
        print(s[i][::-1],end=" ")
    else:
        print(s[i],end=" ")