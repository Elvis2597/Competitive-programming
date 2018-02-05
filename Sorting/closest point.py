left=list(map(int,input().split()))
right=list(map(int,input().split()))
x=int(input())
nL=len(left)
nR=len(right)
A=[0]*(nL+nR)
i=0
j=0
k=0
while(i<nL and j<nR):
    if left[i]<=right[j]:
        A[k]=left[i]
        i+=1
    else:
        A[k]=right[j]
        j+=1
    k+=1
while(i<nL):
        A[k]=left[i]
        i+=1
        k+=1
while(j<nR):
        A[k]=right[j]
        j+=1
        k+=1
diff=1000000
i=0
j=(nL+nR)-1
while(i<nL and j>nL):
    Sum=A[i]+A[j]
    if Sum==x:
        ans=[A[i],A[j]]
        break
    elif Sum>x:
        if abs(x-(Sum))<diff:
            diff=abs(x-(Sum))
            ans=[A[i],A[j]]
        j-=1
    else:
        if abs(x-(Sum))<diff:
            diff=abs(x-(Sum))
            ans=[A[i],A[j]]
        i+=1
print(ans)
