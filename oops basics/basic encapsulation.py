class fam:
    publicdata=10000
    def grand(self,ma):
        self.ma=ma
        print(f"enter {ma} in grand method and {self.publicdata}")
    @staticmethod
    def static(a,b):
        print("sum of two numbers: ",a+b)
    @classmethod
    def child(cls,s1,s2):
        cls.son1=s1
        cls.son2=s2
        x = 10
        y = 20
        print("sum of x and y: ", x + y)
        print(f"we are the children in out family,my name is {s1} , my brother {s2} and {cls.publicdata}")
ob=fam()
ob.grand("anasurya")
ob.child("Saivamshi","Aravind")
ob.static(20,50)
