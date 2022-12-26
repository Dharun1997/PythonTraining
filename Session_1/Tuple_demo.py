mytuple=('balaji','vishnu','tharun','kiran','vinay')
mylist=list(mytuple)
mylist.append('ashwin')
mytuple=tuple(mylist)
print(mytuple)
print('Appending tuple completed')

del mytuple
print('Tuple deleted')

tuple1 = ('kiwi','apple')
tuple2 = ('kiwi','app')
if tuple2==tuple1:
    print('Equal')
else:
    print('Not equal')
