#  Count even and odd digits
num=12345679
even=0
odd=0
n=0
while 0<num:
    n=num%10
    if n%2==0:
        even+=1
    else:
        odd+=1
    num=num//10
print(even)
print(odd)