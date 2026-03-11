# Fibonacci series store karana.

fib = []
a,b=0,1
for i in range(10):
    fib.append(a)
    a,b=b,a+b  # a=0,b=1 hone per a+b=b karane per a=b,b=a+b
print(fib)