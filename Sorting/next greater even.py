def greater(l):
    n=len(l)
    l=list(l)
    flag=0
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            if l[j]<l[i]:
                flag=1
                l[j],l[i]=l[i],l[j]
                break
        if flag==1:
            break
        else:
            continue
    if flag==0:
        return -1
    else:
        l[j+1:]=sorted(l[j+1:])
        return l
for _ in range(int(input())):
    l=input()
    num=greater(l)
    if num==-1:
        print(-1)
    else:
        if int(num[-1]) in [0,2,4,6,8]:
            print("".join(map(str,num)))
        else:
            n=len(num)
            for i in range(n-1,-1,-1):
                if int(num[i])%2==0 and int(num[-1])>int(num[i]):
                    num[i],num[n-1]=num[n-1],num[i]
                    num[i+1:n-1]=sorted(num[i+1:n-1])
                    result="".join(map(str,num))
                    break
            else:
                print(-1)
