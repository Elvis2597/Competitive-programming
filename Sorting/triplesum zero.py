for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in range(n):
        if l[i]<0:
            count+=1
    if count==0:
        print(0)
    else:
        flag=0
        l=sorted(l)
        for i in range(count):
            num=-l[i]
            j=i+1
            k=n-1
            while(j<k):
                Sum=l[j]+l[k]
                if Sum==num:
                   flag=1
                   break
                elif Sum<num:
                    j+=1
                else:
                    k-=1
        print(1 if flag==1 else 0)
    
