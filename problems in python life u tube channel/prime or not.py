n=int(input("enter a number:"))
for i in range(2,int(n)):
    if n%i == 0:
        print("prime")
    if n%i != 0:
        print("not a prime")
    break