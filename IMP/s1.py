# reverce print karana hai
num=int(input("Enter your number : "))
p=0
while(0<num):
        
        n=num%10
        p=(p*10)+n
        num=num//10
print(p)