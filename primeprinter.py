# def prime_checker(n):
#     for i in rang
#         return False
#     return True
#
# for i in range (1,100):
#     if prime_checker(i):
#         print(i)
def isPrime(num = "10"):
    k=2
    for i in range(2,k):
        if (num % i) == 0:
            print("F:is not a prime")
            break
        else:
            print(i)
            k =+1
        if k > num:
            break
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
#take input and confirm
num = int(input('How many prime numbers you would like to get? Please provide a number:'))
index = 1
if num > 100:
    print('Please be careful with high numbers as it may take long to generate')
    decision = input('type Y+enter to continue, press any key+enter to cancel:')
    if decision == 'Y' or 'y':
        print("I decided" + num)
        if is_prime(num) == True:
            print(num)
            index += 1
    else:
        print('Good decision, please run again and choose lower number')
        exit()
else:
    if is_prime(num) == True:
        print(num)
        index += 1
        print(index)

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

#prime number printer
# index = 0
# for i in range(2,num+1):
#     while i < num:
#         count = 0
#         for j in range(2,i):
#             if i%j != 0:
#                 count += 1
#         if count == i-2:
#             print(i)
#         index += 1
