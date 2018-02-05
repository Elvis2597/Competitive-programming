for _ in range(int(input())):
    n1,n2=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    i=0
    j=0
    while(i<n1-1 and j<n2-1):
        if l1[i]>l2[j]:
            print(l1[i],end=" ")
            i+=1
        else:
            print(l2[j],end=" ")
            j+=1
    while(i<n1):
        print(l1[i],end=" ")
    while(j<n2):
        print(l2[j],end=" ")
    print()
