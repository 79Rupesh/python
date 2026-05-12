#  Number Incresing pyramid
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n=5
for i in range(n,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()