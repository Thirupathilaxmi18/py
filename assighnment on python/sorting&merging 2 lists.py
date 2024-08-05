
def addition(list1,list2):
    list1.sort()
    print(list1)
    list2.sort()
    print(list2)
    add=list1+list2
    add.sort()
    print(add)
list1=[5,3,8,2,8,9,2]
list2=[4,8,2,9,2,6,4]
addition(list1,list2)