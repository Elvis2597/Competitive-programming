n=int(input())
l=list(map(int,input().split()))
pos=any(x>0 for x in l)
if pos:
    Sum=0
    ans=-99999
    start=0
    end=0
    s=0
    for i in range(n):
        Sum+=l[i]
        if ans < Sum:
            ans=Sum
            start=s
            end=i
        if Sum<0:
            s=i+1
            Sum=0
        ans=max(Sum,ans)
    print(ans,start,end)
else:
    print(max(l))


"""
10
1 -3 2 -5 7 6 -1 -4 11 -23
19 4 8
"""
