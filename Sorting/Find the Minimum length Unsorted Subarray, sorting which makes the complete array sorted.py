for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        if l[i]>l[i+1]:
            break
    for j in range(n-1,0,-1):
        if l[j]<l[j-1]:
            break
    if i==n-2 or j<1:
        print(0,0)
    else:
        minimum=min(l[i:])
        maximum=max(l[0:j])
        while(minimum<l[i] and i>=0):
            i-=1
        while(j<=n-1 and maximum>l[j]):
            j+=1
        print(i+1,j-1)
