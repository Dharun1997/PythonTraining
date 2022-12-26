weekday = int(input('Enter weekday : '))

if weekday==1:
    print('Sunday')
elif weekday==2:
    print('Monday')
else:
    print('Tuesday')

#if else in a single statement using Ternary operator

age = 20
print('Not eligible for voting') if age<=18 else print('Eligible for voting')

