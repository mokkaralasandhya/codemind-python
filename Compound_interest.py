import math
a,b,c=map(int,input().split())
f=a*(math.pow((1+b/100),c))
print("%.2f"%f)