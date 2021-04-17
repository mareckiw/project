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
print(list1[1][5:7])
list2 = [143242,432432543,4324324,2423124,4351,1341,1]
list3 = []
for elem in list2:
    list3.append(elem * 2)
print(list3)

list4 = [x*2 for x in list1]
print(list4)

d1 = {'a': 10, 'b':11, 'c':12}
print(list(d1.keys())[0])
print(d1['a'])
print(list(d1.values()))
print(list(d1.keys()))
for key in d1.keys():
    print(d1[key])

my_file = 'mickiewicz.txt'
i = 0
with open(my_file, 'r',encoding='utf-8') as f:
    lines = f.readline()
    for line in lines:
        i =+1
        print("%i: %s" % (i,line))

#homework - simple text file and count num