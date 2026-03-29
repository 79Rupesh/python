# check if a number is palindrom
num=121
temp=num
rev=0
n=0
while 0<num:
    n=num%10
    rev=(rev*10)+n
    num=num//10
    
if temp==rev:
    print("palindrom number")
else:
    print("not palindrom")