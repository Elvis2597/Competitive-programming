import collections
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    M=int(input())
    l=sorted(l)
    dict=collections.Counter(l)
    print(dict)
    dict=sorted(dict,key=lambda x:x[1])
    i=0
    while(M>0):
        M-=dict[i][1]
        i+=1
    if M==0:
        print(len(dict)-(i))
    else:
        print(len(dict)-(i-1))
