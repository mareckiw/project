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
lim = int(input('How many prime numbers you would like to get? Please provide a number:'))
index = 0
while index < lim:
    if is_prime(num) == True:
        print(is_prime(num))
        index += 1
