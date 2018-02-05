for i in range(int(input())):
    x,n=list(map(int,input().split()))
    l=list(range(1,n+1))
    Sum=(n*(n+1))//2-x
    if Sum%2==0 and Sum>4:
        Sum=Sum//2
        result=[0]*n
        i=n-1
        result[x-1]=2
        checksum=0
        flag=0
        while(i>0):
            if l[i]==x:
                i-=1
            else:
                checksum+=l[i]
                if checksum==Sum:
                    result[i]=1
                    break
                elif checksum<Sum:
                    result[i]=1
                    i-=1
                else:
                    num=Sum-(checksum-l[i])
                    if num==x:
                        if num>=3:
                            result[i]=0
                            result[num-2]=1
                            result[0]=1
                            break
                        elif num==1:
                            result[1]=1
                            result[i+1]=0
                            result[i]=1
                            break
                        elif num==2:
                            result[2]=1
                            result[i+1]=0
                            result[i]=1
                            break
                        else:
                            flag=1
                            break
                    else:
                        result[num-1]=1
                        break
        if flag==1:
            print('impossible')
        else:
            print("".join(map(str,result)))
    else:
        print('impossible')
