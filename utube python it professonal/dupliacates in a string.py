'''str=input("enter a string:")
duplicates=' '
for i in str:
    if i not in duplicates:
        duplicates=duplicates+i
print("duplicates:",duplicates)'''


def nodup(str):
    without = ''
    for i in str:
        if i not in without:
         without=without+i
    print("without duplicates:",without)
def dup(str):
    repeat = ' '
    count=0
    for i in str:
        count+=1
        if count>1:
            repeat=repeat+i
    print("repeated:",repeat)
str1=input("enter fst string:")
str2=input("enter second string:")
nodup(str1)
dup(str2)
