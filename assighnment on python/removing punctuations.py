def remove_puct(str):
    for i in str:
        if i is str.isalpha():
          return i
name=input("enter a name:")
li=remove_puct(name)
print(li)