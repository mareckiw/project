from pip._vendor.msgpack.fallback import xrange

p = True
q = False

if p and q:
    print('p and q = TRUE')
else:
    print('NOTTRUE p nor q')

#xor
if p ^ q:
    print('p xor q = TRUE')
else:
    print('p xor q = NOT TRUE')

for i in range (10):
    if i==3:
        continue
        #pass
    print(i)
    if i==7:
        break
#pass is used when you want to ignore an exception for example, to do nothing in this case generally its like open and close brackets

def sum (a, b):
    return a + b
print(sum(55,420))

# homework1
# function to check and print n first prime numbers (1,3,5,7,11,13,17,23)
from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
is_prime(bool(5))