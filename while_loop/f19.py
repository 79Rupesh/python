#  Print sum of even numbers from 1 to N📥
#  Input: 10 → 📤 Output: 30
n = 10
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)