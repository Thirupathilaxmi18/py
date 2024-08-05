n=int(input("enter any year number:"))
if n%400==0 or n%100!=0 and n%4==0:
    print("leap year")
else:
    print("not a leap year")