d,m,y=map(int,input("enter a date -").split("/"))
if(m%2==0 and d<=30 and m!=2):
    print("it is a vaid date")
elif(m%2==1 and d<=31):
    print("it is a valid date")
elif(m==2):
    if(d<=28):
        print("it is a valid date")
    elif(d==29):
        if((y%4==0 and y%400==0)or(y%100!=0)):
            print("it is a valid date")
        else:
            print("it is not a valid date")
else:
    print("it is not a valid date")
        

    