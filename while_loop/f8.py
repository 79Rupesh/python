# Print digits of a number (last to first)
num=123
n=0
while 0<num:
    n=num%10
    num=num//10
    print(n,end=" ")