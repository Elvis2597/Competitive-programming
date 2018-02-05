n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
flag=0
for i in range(n-2):
   j=i+1
   k=n-1
   while(j<k):
       if (l[i]+l[j]+l[k])==m:
           flag=1
           break
       elif (l[i]+l[j]+l[k])>m:
            k-=1
       else:
            j+=1
print(1 if flag==1 else 0)
