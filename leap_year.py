year=int(input("enter a year"))
if((year%4==0 and year%100!=0) or year%400==0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")
print("my name is parth")