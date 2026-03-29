# Reverse a number
num=1234
rev=0
while 0<num:
    rev=num%10
    
    num=num//10
    print(rev,end=" ")