# Sum of digits
num=123456
sum=0
n=0
while 0<num:
    n=num%10
    sum=sum+n
    num=num//10
print(sum)
