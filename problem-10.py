x=int(input("enter number "))
y=int(input("enter number "))
for a in range(1,x*y,1):
    if(x%a==0 and y%a==0):
        hcf=a
print(hcf)
