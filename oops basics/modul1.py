from abc import abstractmethod
class cars:
    def __init__(self,seseater,fiseater):
        self.seseater=seseater
        self.fiseater=fiseater
    @abstractmethod
    def sevenseater(self):
       print(self.seseater," \n", self.fiseater)
class bikes:
    def bike1(self):
        print("fst module: platinum")
    @abstractmethod
    def bike2(self):
        print("fst  module: hero honda")
ob=cars("safari","punch")
ob.sevenseater()
ob1=bikes()
ob1.bike2()
ob1.bike1()