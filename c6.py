#python variables are visible to the upper levels - nice!
#this applies ONLY to BLOCK, not to FUNCTIONs!
#python variables are only visible in one function

b=10
while True:
    print(b)
    b +=1
    if b>15:
        break
#same but condition in while already -> shorter
while b<15:
    print(b)
    b +=1

list1 = [143242,432432543,4324324,2423124,4351,1341,1]

for elem in list1:
    print(elem)
    print('Element %a at position %d' %(elem,list1.index(elem)))

list1.sort()
list1.append('123')
list1.insert(1,'drugiemiejsce')
print(list1)