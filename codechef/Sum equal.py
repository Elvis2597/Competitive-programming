from collections import deque
for _ in range(int(input())):
    x,n=list(map(int,input().split()))
    li=list(range(1,n+1))
    l=list(range(1,x))+list(range(x+1,n+1))
    listsum=sum(l)
    cmp=listsum//2
    if listsum%2==0:
        i=0
        Sum=deque()
        Sum.append(l[0])
        while(i<n-1 and Sum):
            cmpsum=sum(Sum)
            if cmpsum==cmp:
                break
            elif cmpsum<cmp:
                i+=1
                try:
                    Sum.append(l[i])
                except IndexError:
                    pass
            else:
                Sum.popleft()
        if Sum:
            if Sum[0]>1:
                for i in li:
                    if i in Sum:
                        print('1',end="")
                    elif i==x:
                        print('2',end="")
                    else:
                        print('0',end="")
            else:
                for i in li:
                    if i in Sum:
                        print('0',end="")
                    elif i==x:
                        print('2',end="")
                    else:
                        print('1',end="")
        else:
            print('impossible')
        print()
    else:
        print('impossible')
