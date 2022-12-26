
#ID address different memory allocation
str1='Hi'
print(id(str1))
str1=str1+'Bro'
print(id(str1))

#slicing function
str2='badminton'
print(str2[1:3])
print(str2[:5])
print(str2[4:-3])
print('Slicing done')

#ord and chr
print(ord('A'))
print((chr(70)))
print('Ord and chr done')

#max, min, len
print(max(str2))
print(min(str2))
print(len(str2))
print('Max, min, len done')

#in and not in
print('bad'in str2)
print('bad' not in  str2)
print('IN and not in done')

#String comparison
print('tom'=='tom')
print('tom'!='tmo')
print('tom'>'tmo')
print('abc'>'')
print('String comparison done')

#Testing strings
print(str2.isalnum())
print(str2.isalpha())
print(str2.isdigit())
print(str2.isidentifier())
print(str2.islower())
print(str2.isupper())
print(str2.isspace())
print('Testing strings done')

#Converting strings
s='Shuttle'
s1=print(s.capitalize())
s2=print(s.title())
s3=print(s.lower())
s4=print(s.upper())
s5=print(s.swapcase())
s6=print(s.replace('tt','nn'))
print('String conversion done')

#Reversing a string method 1
rev_str=s[::-1]
print(rev_str)

#Reversing a string method 2
rev_str=''
for i in s:
    rev_str=i+rev_str
print('Reversed string is : ',rev_str)


