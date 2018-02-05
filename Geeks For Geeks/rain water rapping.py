n=int(input())
l=list(map(int,input().split()))
R=[]
L=[]
Sum=0
for i in range(n):
    L.append(max(l[0:i+1]))
    R.append(max(l[i:n]))
for i in range(n):
    Sum+=min(L[i],R[i])-l[i]
print(Sum)
