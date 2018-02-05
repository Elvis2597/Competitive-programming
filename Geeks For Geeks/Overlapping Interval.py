import functools
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=[]
    for i in range(0,2*n,2):
        m.append([l[i],l[i+1]])
    m=sorted(m)
    li=functools.reduce(lambda x,y: x+y,m)
    i=0
    j=1
    while(j<2*n-1):
        if li[j+1]<li[i+1]:
            j+=1
        else:
            if j%2==0:
                print(l[i],max(l[i+1],l[j+1]),end=" ")
                j+=2
                i=j
                j=j+1
            else:
                print(l[i],max(l[i+1],l[j]),end=" ")
                j+=1
                i=j
                j=j+1
    try:
        print(li[i],max(li[i+1],li[j]))
    except IndexError:
        pass
