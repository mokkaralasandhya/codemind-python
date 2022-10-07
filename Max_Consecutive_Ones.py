def getmaxlength(arr,n):
    count=0
    #initialize max
    result=0
    for i in range(0,n):
        #reset count when 0 is found
        if (arr[i]==0):
            count=0
        else:
            count+=1
            result=max(result,count)
    return result
n=int(input())
a=list(map(int,input().split()))
print(getmaxlength(a,n))