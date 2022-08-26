for i in range(2,101,1):
    flag=0
    for a in range(2,(i//2+1)):
        if i%a==0:
            break
    else:
        print(i)
