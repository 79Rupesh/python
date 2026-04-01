# GCD of two numbers using subtraction📥
#  Input: 12, 15 → 📤 Output: 3
a=12
b=15
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)