dict1={'Name':'Dharun',
       'Age': 26,
        'Passion': 'Badminton'}
dict1['Name']='Tharun'
print(dict1)
print(dict1.get('Age'))

for i in dict1:
    print(i) #prints only keys

for i in dict1.values():
    print(i) #prints only values

for x,y in dict1.items():
    print(x,y) #prints key and values

#insertion
dict1['Job']='IT'
print('Insertion done')

#deletion
dict1.pop('Passion')
del dict1['Job']
print(dict1)

#copying
dict2=dict1.copy()
print(dict2)






