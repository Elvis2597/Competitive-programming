for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    lis=[1]*n
    i=1
    j=0
    while(i<n):
        print(i)
        while(j<i):
            print(j)
            if l[j]<l[i]:
                print(lis)
                lis[i]=max(lis[i],lis[j]+1)
            j+=1
        i+=1
        j=0
    print(max(lis))
