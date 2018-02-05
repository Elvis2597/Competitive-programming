for i in range(int(input())):
    x,n=list(map(int,input().split()))
    l=list(range(1,n+1))
    l.remove(x)
    Sum=sum(l)
    if Sum%2==0:
        Sum=Sum//2
        result=[0]*n
        i=n-1
        result[x-1]=2
        checksum=0
        flag=0
        while(i>=0):
            p=l.pop()
            checksum+=p
            if checksum==Sum:
                result[p-1]=1
                break
            elif checksum<Sum:
                result[p-1]=1
                i-=1
            else:
                num=Sum-(checksum-p)
                if num!=x:
                    result[num-1]=1
                    break
                else:
                    if num==1:
                        result[1]=2
                        result[num-2]=1
                        break
                    else:
                        flag=1
                        break 
        if flag==1:
            print('impossible')
        else:
            print("".join(map(str,result)))
    else:
        print('impossible')
