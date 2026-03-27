# check is the prime number
num = 13
isprime = True
i = 2

# Step 1: check for numbers <=1
if num <= 1:
    isprime = False

# Step 2: loop check
while i < num:
    if num % i == 0:
        isprime = False
        break
    i += 1   # step 3: increment

# Step 4: output
if isprime:
    print("prime number")
else:
    print("not prime")