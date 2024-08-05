class Institute:
    def __init__(self,name,role):
        self.name=name
        self.role=role
class Inside(Institute):
    def employee1(self):
        print(f"{self.name} is  employee, his/her role is {self.role} ")
class Developer(Inside):
    def employee2(self,qualification):
        self.qualification=qualification
        print(f"{self.name} is  employee, his/her role is {self.role} and qualification {qualification} ")
obj=Inside("laxmi","python develper")
obj.employee1()
obj2=Developer("Geetha","Tester")
obj2.qualification="b.tech"
# obj2.employee2()
obj2.employee2(obj2.qualification)