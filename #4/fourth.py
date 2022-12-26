from math import *
a = input("Iput first number: ")
if not a.isdigit():
    print("string value cannot be entered")
    print("or number is negative, restart the program")
    exit()
else:
    a = int(a)
if a==0:
    print("the number cannot be zero");input()
count = 0;
ar=0;
while True:
    ar+=a; count+=1
    try:
        a=int(input("Input next number or Enter 0 to finish: "))
    except:
        print("string value cannot be entered")
        print("or number is negative, restart the program")
        exit()
    else:
        if a==0:
            break
ar = ar/count
print("Average : ",ar)