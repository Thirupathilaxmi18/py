n1,n2,n3=map(int,input("enter a number:").split(","))
if n1<n2 and n1<n3:
    print(f"{n1} is smallest among them")
elif n2<n3 and n2<n1:
    print(f"{n2} is smmalest number among them")
else:
    print(f"{n3} is smallest numebr among them")
