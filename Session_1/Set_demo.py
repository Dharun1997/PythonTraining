myset={'adidas','reebok','puma','nike'}
myset.add('mrf')
myset.update(['lining','yonex'])
print(myset)
print('Insertion done')

#remove and discard
myset.remove('reebok')
#myset.remove('xyz') #will throw Keyerror
myset.discard('puma')
myset.discard('xyz') #not throw error
print(myset)
print('remove and discard done')

#joining sets
set1={'Tharun'}
set2={'Shuttler'}
set3=set1.union(set2)
print(set3)
set1.update(myset)
print(set1)
