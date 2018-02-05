n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
count=0
i=0
j=0
while(count<n-1):
    if l1[i]<l2[j]:
        i+=1
    else:
        j+=1
    count+=1
    print(count)
print((l1[i]+l2[j])/2)
