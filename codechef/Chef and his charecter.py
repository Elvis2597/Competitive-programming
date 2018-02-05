for _ in range(int(input())):
    s=input()
    count=0
    for i in range(len(s)-3):
        l=set(s[i:i+4])
        if l=={'c','h','e','f'}:
            count+=1
    if count==0:
        print('normal')
    else:
        print('lovely '+str(count))
        
