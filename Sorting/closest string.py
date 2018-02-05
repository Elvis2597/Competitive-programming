for _ in range(int(input())):
    n=int(input())
    l=input().split()
    w1,w2=input().split()
    Min=100000
    word1=[]
    word2=[]
    for i in range(n):
        if l[i]==w1:
            word1.append(i)
        if l[i]==w2:
            word2.append(i)
    for i in word1:
        for j in word2:
            dif=abs(i-j)
            if dif<Min:
                Min=dif
    print(Min)
