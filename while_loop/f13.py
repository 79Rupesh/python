# Check if a number is Armstrong.
num=153
number=num
multi=0
n=0
while 0<num:
    n=num%10
    multi = multi+(n*n*n)
    num=num//10


if number==multi:
    print("Arstonge number")
else:
    print("not Arstonge number")