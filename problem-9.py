x=int(input("enter number "))
y=int(input("enter numbr "))
for a in range (x,(x*y)+1,1):
    if(a%x==0 and a%y==0):
        print(a)
        break;
    
