#  Print Fibonacci series (N terms)📥
#  Input: 5 → 📤 Output: 0 1 1 2 3
num=5
a=0
b=1
c=0
i=0
while i<num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1