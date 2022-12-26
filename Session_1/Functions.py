def myfun(a,b):
    return (a+b)

c=myfun(10,20)
print(c)

def fun1():
    return   #returns none
fun1()

#Global and local variables
x=100
def cal():
    global x
    x=200
    print('Value inside function',x)

cal() #if commented then above cal function value will display
print('Value outside function',x)

#Positional and Keyword arguments
def add(a,b,c):
    d=a+b+c
    print(d," "+'is the result')

add(10,20,30)
add(b=30,c=10,a=20)
add(30,b=10,c=20)
#add(30,c=10,20) #throw error because postional argument should come before keyword argument