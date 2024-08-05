# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     # def __repr__(self):
#     #     return "person ('{}')".format(self.msg)
#     def __str__(self):
#         return "{},{} ".format(self.x,self.y)
#
#     def __repr__(self):
#         return "point ('{}'.'{}')".format(self.x,self.y)
# e=Point("hello","welcome")
# print("basic: ",e)
# print(e.__repr__())
# print(e.__str__())
# class Person:
#     def __init__(self,msg):
#         self.msg=msg
#     def __add__(self, string):
#         return self.msg+string
# e=Person("hello")
# print(e+"folks")
# # x=4
# print(x.__floordiv__(3`))
class Employee:
    def __init__(self,string):
        self.string=string
    # def __getitem__(self, item):
    #     return self.string[item]
    def __setitem__(self, key, value):
        self.string[key]=value
e=Employee({1:"laxmi",2:"sneha",3:"chitti"})
print(e.string)
e[2]="pavani"
print(e.string)
e[4]="lakshmi"
print(e.string)














