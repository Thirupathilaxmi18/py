str=input("enter a  name: ")
vowels='a','e','i','o','u'
v1=''
c1=''
for ch in str:
    if ch in vowels:
        v1+=ch
    else:
        c1+=ch
print("vowels :",v1)
print("consonent :",c1)