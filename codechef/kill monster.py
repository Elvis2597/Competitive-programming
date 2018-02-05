n=int(input())
l=list(map(int,input().split()))
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    for k in range(n):
        if k&x==k:
                l[k]-=y
    count=0
    for j in l:
        if j>0:
            count+=1
    print(count)
        
        
