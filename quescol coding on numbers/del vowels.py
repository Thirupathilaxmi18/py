str=input("enter a string :")
vowels="a","e","i","o","u"
del_vow=""
for ch in str:
    if ch== " ":
        pass
    elif ch in vowels:
        pass
    else:
        del_vow=del_vow+ch
print(del_vow,"deleted")