a=int(input())
if a in range(3,100):
    for i in range(1,a+1):
        print('*'*i)
    for i in range(a-1,0,-1):
        print('*'*i)
else:
    print('The pattern is not possible')