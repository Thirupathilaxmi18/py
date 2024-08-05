from abc import abstractmethod
import modul1
class cars:
    @abstractmethod
    def sevenseater(self):
        print("it is in second module: running")
class plain:
    def airlines(self):
        print("it is in second module : walking")
# ob=modul1.cars("safari","punch")
# # ob.sevenseater()
# ob2=modul1.bikes()
# ob2.bike1()
# ob2.bike2()
ob3=plain()
ob3.airlines()
ob4=cars()
ob4.sevenseater()