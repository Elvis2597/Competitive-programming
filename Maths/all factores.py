n=int(input())
l=[]
m=[]
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        l.append(i)
        m.append(n//i)
if i!=int(n**(1/2)):
    print(l+m[::-1])
else:
    print(l[:-1]+m[::-1])
