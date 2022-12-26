#writing into file
file=open("C:/Users/DHARUN R/Desktop/file1.txt",'w')
file.write('This is first line..\n')
file.write('This is second line..\n')
file.close()

#reading into file
file1=open("C:/Users/DHARUN R/Desktop/file1.txt",'r')
print(file1.read())
file1.close()

#appending into file
file2=open("C:/Users/DHARUN R/Desktop/file1.txt",'a',)
file2.write('This is appended line')
file2.close()




