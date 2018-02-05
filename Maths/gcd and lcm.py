a,b=map(int,input().split())
if a>=b:
    dividend=a
    divisor=b
else:
    dividend=b
    divisor=a
while(divisor!=0):
    reminder=dividend%divisor
    dividend=divisor
    divisor=reminder
gcd=dividend
# num1*num2=LCM*GCD
lcm=a*b//gcd
print('gcd is',gcd)
print('lcm is',lcm)
