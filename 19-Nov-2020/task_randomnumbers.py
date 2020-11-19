import random
c=0
for i in range(1,4):
    a=int(input("enter you are guessing number"))
    b=random.randint(1,10)
    if a==b:
        c=c+1
    print(i,     a,        b)    
if(c!=1):
    print("better luck next time")
