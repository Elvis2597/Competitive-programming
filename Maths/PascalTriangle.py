P=[[1]]
n=int(input())
for i in range(n-1):
    L=[]
    K=P[-1]
    L.append(1)
    for j in range(i):
        L.append(K[j]+K[j+1])
    L.append(1)
    P.append(L)
print(" ".join(map(str,P[-1])))
