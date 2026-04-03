# Find LCM of two numbers📥
#  Input: 4, 5 → 📤 Output: 20

a = 15
b = 12

if a > b:
    i = a
else:
    i = b

while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1