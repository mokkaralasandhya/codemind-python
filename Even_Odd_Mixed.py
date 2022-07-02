n=int(input())
s=0
even=0
odd=0
while n>0:
    r=n%10;
    s+=1
    if(r%2==0):
        even+=1
    else:
        odd+=1
    n//=10
if(odd==s):
    print("Odd")
elif(even==s):
    print("Even")
else:
    print("Mixed")
    