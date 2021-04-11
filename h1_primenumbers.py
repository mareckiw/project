from itertools import count
lim = int(input('How many prime numbers you would like to get? Please provide a number:'))
# prime number printer
index = 0
for i in count():
    count = 0
    for j in range(2, i):
        if i % j != 0:
            count += 1
    if count == i - 2:
        if index == 0:
            print(index + 1, "st prime number:", i)
        elif index == 1:
            print(index + 1, "nd prime number:", i)
        else:
            print(index + 1, "th prime number:", i)
        index += 1
        if index + 1 > lim:
            break
