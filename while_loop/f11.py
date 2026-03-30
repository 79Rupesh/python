# Product of digits📥
#  Input: 123 → 📤Output: 6
num=123
n=1
product=1
while 0<num:
    n=num%10
    product=product*n
    num=num//10
print(product)