x=int(input("enter a number "))
for i in range(3,x):
    if(x%i==0):
        print("non-prime number")
        break;
else:

    print("prime number")
