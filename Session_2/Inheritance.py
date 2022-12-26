# single inheritance and method,variable overriding
class A:
    x,y=10,20
    def f1(self):
        print("This is from class A")
class B(A):
    def f1(self):
        super().f1()
        print("This is from class B")
        print(self.x+self.y)
obj1=B()
obj1.f1()

#polymorphism/Overloading

class Cal:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Cal()
calobj.add()
calobj.add(10,20)
calobj.add(50,50,50)




