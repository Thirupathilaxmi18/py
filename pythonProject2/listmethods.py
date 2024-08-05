mylist=[10,20,30,40,50,"sneha"]
print("mylist",mylist)
for i in mylist:
    print(i)
mylist.append("chitti")
print("after appending chiti into mylist",mylist)
newlist=mylist.copy()                #coping of list
print("mylist is coping into the newlist:",newlist)
mylist.clear()  #to clear all the elements in the list
print("cleaing mylist elements:",mylist)
for i in range(1,30,2):
    mylist.append(i)            #adding elements
print("created list using range:",mylist)
mylist.remove(9)               #
print("removing 9 from mylist:",mylist)
print("index method:",mylist.index(5))
print("pop methd",mylist.pop())
print(" pop,index,removing mylist:",mylist)
mylist.remove(1)
print("removing method:",mylist)
mylist.append(21)
mylist.append(21)
mylist.append(23)
print("appending values:",mylist)
#03/07/2024
mylist=[10,20,30,40,"sneha"]
print(mylist[3])
print(mylist)
mylist.append("chitti")
print(mylist)
mylist.insert(6,"laxmi")
print(mylist)
mylist.pop()
mylist.pop()
mylist.pop()
print("poping strings from the list:",mylist)
mylist.reverse()
print("reversed list:",mylist)
mylist.sort()
print("sorted list:",mylist)
mylist.extend(mylist)
mylist.extend(mylist)
print("extending mylist 2 times:",mylist)
print("10 count:",mylist.count(10))
