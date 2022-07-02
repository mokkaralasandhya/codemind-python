n=int(input())
count=0
for i in range(1,n):
    if(i*i==n):
        count+=1
if count>0:
    print("True")
else:
    print("False")