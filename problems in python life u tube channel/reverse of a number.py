n=int(input("enter a number:"))
temp=n
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
print(reverse)
