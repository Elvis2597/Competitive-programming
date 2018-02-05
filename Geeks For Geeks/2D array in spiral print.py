m,n=4,4
l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
dirc=0
T=0
B=m-1
L=0
R=n-1
while(T<=B and L<=R):
    if dirc==0:
        for i in range(L,R+1):
            print(l[T][i])
        T+=1
    elif dirc==1:
        for i in range(T,B+1):
            print(l[i][R])
        R-=1
    elif dirc==2:
        for i in range(R,L-1,-1):
            print(l[B][i])
        B-=1
    elif dirc==3:
        for i in range(B,T-1,-1):
            print(l[i][L])
        L+=1
    dirc=(dirc+1)%4
