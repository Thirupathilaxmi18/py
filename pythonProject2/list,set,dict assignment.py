'''3. Write a program which prints numbers in range 1,100 which are divisible by 5'''
print("answer of 3 question")
print("fst trial")
for i in range(1,100,5):
    print(i)
print("trial 2")
for i in range(1,100):
     if i%5==0:
        print(i)
print("trial 3")
for i in range(100):
    if i%5==0:
        print(i)
'''2. Create a list of length 10 including numbers and strings
	a. Slice the list till the index 8
	b. Print the element which is located at index 8
	c. Perofrm sort and reverse operations on the list 
	d. Write a program which takes string as input and reverses that string 
'''
print("second answer")
ls=[1,2.0,"laxmi",1+3j,3,4,5,6,1,2]
print("2a.slicing the list",ls[:8])
element8=ls[8]
print("2b.printing eleemnt8",element8)
ls.reverse()
print("2c.reversed list:",ls)
ls.reverse()
print("original list:",ls)
ls.pop(2)
ls.pop(2)
print(ls)
ls.sort()
print("2c sortedlist:",ls)
#
#
str=input("enter a string:")
print(str[::-1])
#
name=input("enter a string to reverse it:")
reversed_name=""
for i  in name:
    reversed_name=i+reversed_name
    print(i)
print(f"reversed string:{reversed_name}")
'''1. Write a python program to print only dictionary keys and values separately.Take a dictionary with 5 items (Key-Value Pairs)
	a. From the above dictionary pop or remove the last element 
	b. Take dictionary from 1.a and add the following key & pair i;e "car":"Tesla" to the dictionary if the key exsists then it should update the value otherwise it should add the Key
	c.Convert the dictionary to List'''
dict={1:"sneha",2:"chitti",3:"pavani",4:"laxmi",5:"navya"}
print("total dictionary:",dict)
print("dict keys using just method:",dict.keys())
for i in dict.keys():
    print("dict keys using for:",i)
print("dict values using just method:",dict.values())
for i in dict.values():
    print("dict values using for:",i)
print(dict.pop(4))
print("1a,",dict)
dict.update({"car":"Tesla"
             })
print("after update:",dict)
print(list(dict))