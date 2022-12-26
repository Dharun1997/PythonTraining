a,b=30,40

class Sample:
    x,y=10,20
    def add(self,a,b):
        print(a+b)
        print(self.x+self.y)
    @staticmethod
    def mul(self):
        print(globals()['a']*globals()['b'])

obj1=Sample()
obj1.add(10,20)
Sample.mul(1)

class Const:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def display(self):
        print(self.eid,self.ename)

ob=Const(2399186,'Dharun')
ob.display()








