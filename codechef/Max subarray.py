def maxsub(l):
    Sum=0
    ans=0
    for i in l:
        Sum=max(i,Sum+i)
        ans=max(ans,Sum)
    return ans
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ispos=all(x>=0 for x in l)
    isneg=all(x<=0 for x in l)
    if ispos:
        print(k*sum(l))
    elif isneg:
        print(max(l))
    else:
        if k<4:
            l=l*k
            print(maxsub(l))
        else:
            num1=maxsub(l*2)
            num2=maxsub(l*3)
            if num1==num2:
                print(num1)
            else:
                print((num1+(num2-num1)*(k-2)))
