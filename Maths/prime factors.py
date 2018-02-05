def prime(n):
    i=2
    fact=[]
    while(i*i<=n):
        if n%i==0:
            fact.append(i)
            n//=i
        else:
            i+=1
    fact.append(n)
    return fact
n=int(input())
result=prime(n)
print(result)
