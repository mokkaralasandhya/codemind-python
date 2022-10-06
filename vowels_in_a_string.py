a=input()
s=input()
if s in a:
    print(True)
for i in range(len(a)):
    if s in a[i]:
        print(i)
        break
else:
    print(False)