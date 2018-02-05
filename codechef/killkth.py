s=input()
n=len(s)
l=[]
for i in range(n):
    for j in range(i,n):
        l.append(s[i:j+1])
l="".join(sorted(l))
G=0
for i in range(int(input())):
    P,M=map(int,input().split())
    K=((P*G)%M) + 1
    y=(l[K-1])
    G+=ord(y)
    print(y)
 
