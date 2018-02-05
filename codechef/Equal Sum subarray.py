def subArraySum(arr, n, Sum):
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > Sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == Sum:
            return l[start:i+1]
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    return []
for i in range(int(input())):
    x,n=list(map(int,input().split()))
    l=list(range(1,n+1))
    li=l[:]
    l.remove(x)
    Sum=sum(l)
    i=0
    j=n-1
    if Sum%2!=0:
        print('impossible')
    else:
        newl1=subArraySum(l,n-1,Sum//2)
        newl2=list(set(l)-set(newl1))
        s=""
        if newl1:
            if newl1[0]<newl2[0]:
                for i in li:
                    if i in newl1:
                        s=s+'0'
                    elif i==x:
                        s=s+'2'
                    else:
                        s=s+'1'
            print(s)
        else:
            print('imposible')
