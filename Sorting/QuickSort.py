def Partition(A,start,end):
    pivot=A[end]
    pindex=start
    for i in range(start,end):
        if A[i]<=pivot:
            A[i],A[pindex]=A[pindex],A[i]
            pindex+=1
    A[pindex],A[end]=A[end],A[pindex]
    return pindex
    
def QuickSort(A,start,end):
    if start>end:
        return
    else:
        pindex=Partition(A,start,end)
        QuickSort(A,start,pindex-1)
        QuickSort(A,pindex+1,end)

l=list(map(int,input().split()))
QuickSort(l,0,len(l)-1)
print(l)
