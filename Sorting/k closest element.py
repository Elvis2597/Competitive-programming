from collections import deque
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k,m=map(int,input().split())
    d=deque()
    j=0
    for i in range(n):
       if l[i]==m:
           continue
       elif i<k:
           d.append(abs(l[i]-m))
       else:
           if abs(l[i]-m)<d[0]:
               d.append(abs(l[i]-m))
               j+=1
               d.popleft()
           else:
               break
    print(d)
