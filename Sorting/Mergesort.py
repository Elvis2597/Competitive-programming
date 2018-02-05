def merge(left,right,A):
    nL=len(left)
    nR=len(right)
    i=0
    j=0
    k=0
    while(i<nL and j<nR):
        if left[i]<right[j]:
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
            
def MergeSort(A):
    n=len(A)
    if n<2:
        return
    else:
        mid=n//2
        left=A[0:mid]
        right=A[mid:n]
    MergeSort(left)
    MergeSort(right)
    merge(left,right,A)
A=list(map(int,input().split()))
MergeSort(A)
print(A)
