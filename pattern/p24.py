# A B C D
# A B C
# A B
# A

n=5
for i in range(n,0,-1):
    ch='A'
    for j in range(1,i):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
        
    print()