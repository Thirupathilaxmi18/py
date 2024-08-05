number=int(input("enter a number:"))
temp=number
n=len(str(number))
reverse=0
while temp!=0:
    digit=temp%10
    reverse=reverse+digit**n
    temp=temp//10
print(reverse)
if number == reverse:
    print(f"yes,{number} is a armstrong number")
else:
    print(f"no,{number} is not a armstrong number")