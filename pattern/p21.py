#  palindrom triangular
#      1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for k in range(2,i+1):
        print(k,end=" ")
    print()