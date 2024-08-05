# .Create a Python class MathOperations with static methods for basic mathematical
# operations such as addition, subtraction, multiplication,and division. Also, include
# a class variable PI for the value of pi
class MathOperations:
    PI=3.14
    @staticmethod
    def addition(x,y):
        print("addition: ",x+y)
    @staticmethod
    def subtraction(x,y):
        print("subtraction: ",x-y)
    @staticmethod
    def multiplication(x,y):
        print("multiplication: ",x*y)
    @staticmethod
    def division(x,y):
        print("division: ",x/y)
ob=MathOperations()
ob.addition(2,3)
ob.subtraction(3,2)
ob.multiplication(5,4)
ob.division(10,5)
