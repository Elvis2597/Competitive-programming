for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    dict=[]
    s=set(l)
    for i in s:
        dict.append([i,l.count(i)])
    dict=sorted(dict,key=lambda x:x[1])
    m=len(s)
    if m==1:
        ans=dict[0][0]
    for i in range(m-1):
        if dict[i+1][1]>dict[i][1]:
            ans=dict[i+1][0]
    print(ans)
