num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result=num1/num2
try:
    if result==0:
        print("Result is",result)
except ZeroDivisionError:
    print("Number cannot be divided by zero")
else:
    print("Number divided",result)
finally:
    print("Program completed")



