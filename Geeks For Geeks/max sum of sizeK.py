for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    maxsum=[l[0]]
    currsum=l[0]
    for i in range(1,n):
        currsum=max(currsum+l[i],l[i])
        maxsum.append(currsum)
    Sum=sum(l[:k])
    result=Sum
    for i in range(k,n):
        Sum=Sum+l[i]-l[i-k]
        result=max(result,Sum)
        result=max(result,Sum+maxsum[i-k])
    print(result)
