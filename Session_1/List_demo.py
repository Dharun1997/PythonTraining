mylist=['apple','mango','orange']
print(mylist[-2:-1])

for i in mylist:
    print(i)

if 'apple' in mylist:
    print('Found')
else:
    print('Not Found')

#append and insert
mylist.append('cherry')
print(mylist)
mylist.insert(1,'kiwi')
print(mylist)
print("Append and insert completed")

#pop, del, clear
mylist.pop(1)
print(mylist)
del mylist[2]
print(mylist)
mylist.clear()
print(mylist)
print('Deletion completed')

#copy list
mylist=['apple','mango','orange']
mylist1=list(mylist)
print(mylist1)
mylist2=mylist1.copy()
print(mylist2)
print('Copying list completed')

#combine list
list1 = ['a','b','c']
list2 = ['1','2','3']
list3 = list1+list2
print(list3)
list3.extend(list1)
print(list3)
print('Combine list completed')




