# sum of digit 
num=12345
sum=0
while(0<num):
    n=num%10
    sum=sum+n
    num=num//10
print(sum)