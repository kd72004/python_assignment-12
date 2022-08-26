x=int(input("enter first number ->"))
y=int(input("enter second number -> "))
for i in range(x,y+1,1):
    for a in range(2,(i//2+1)):
        if(i%a==0):
            break;
    else:
        print(a)
