for _ in range(int(input())):
    s=list(input())
    l=list(map(int,s))
    n=len(l)
    ans=False
    while True:
        pos=-1
        for i in range(n-2,-1,-1):
            if l[i]<l[i+1]:
                pos=i
                break
        if pos==-1:
            ans=False
            break
        else:
            j=l.index(min(l[pos+1:]))
            l[j],l[pos]=l[pos],l[j]
            l[pos+1:]=sorted(l[pos+1:])
        if l[-1]%2==0:
            ans="".join(map(str,l))
            break
    if ans:
        print(ans)
    else:
        print(-1)
        
