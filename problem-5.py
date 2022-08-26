x=int(input("enter a number "))
for i in range(x+1,x+20,1):
    for a in range(2,(i//2+1)):
        if i%a==0:
            break;
    else:
        print(i)
        break;
