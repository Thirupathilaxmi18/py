class Messages:
    def welcome(self,hi,hello):
        self.hi=hi
        self.hello=hello
        return hi
    def sendoff(self,bye,takecare):
        self.bye=bye
        self.takecare=takecare
        return bye,takecare
class calls:
    def incoming(self,accepted,rejected):
        self.accepted=accepted
        self.rejected=rejected
        return accepted,rejected
    @classmethod
    def outgoing(cls,sim1,sim2):
        cls.sim1=sim1
        cls.sim2=sim2
        return sim1+sim2
    @staticmethod
    def favourites(mom,dad):
        mom=input("enter name: ",mom)
        dad=input("enter dad: ",dad)
        print(f"static method:{mom}&{dad}")
    def sendoff(self,goodbye,sweetdreams):
        self.goodbye=goodbye
        self.sweetdreams=sweetdreams
        return goodbye ,sweetdreams
ob=Messages()
print(ob.welcome("oy"))
print(ob.sendoff("bye","takecare"))
ob2=calls()
# print(ob2.favourites("parvathi","ramanarsaiah"))
print(ob.sendoff("goodnight","sweetdreams"))
