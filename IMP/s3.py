# palindrome number 
num=121
rev=0
tem=num
while(0<num):
    n=num%10
    rev=(rev*10)+n
    num=num//10


if(tem==rev):
    print("palindrome number")
else:
    print("not palindrome number")