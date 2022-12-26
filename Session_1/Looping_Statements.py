i=1

while i<=5:
    print(i)
    i=i+1
print('While loop completed')

j=1
k=10

for j in range(j,k):
    if j==5:
        break
    print(j)
print('Break done')

j=1

for j in range(j,k):
    if j==5:
        continue
    print(j)
print('Continue done')