# Using Segmented Sieve approach
from math import sqrt, floor


def get_primes_till_a_number(n):
    numbers = [True] * (n-1)
    for num in range(2, n+1):
        if numbers[num-2]:
            for num2 in range(num*2, n+1, num):
                numbers[num2-2] = False
    primes_of_sqrt = []
    index = 2
    for num in numbers:
        if num:
            primes_of_sqrt.append(index)
        index = index + 1
    return primes_of_sqrt


def get_primes_in_range(x, y):
    primes_till_square = get_primes_till_a_number(int(sqrt(y)))
    numbers = [True] * (y - x + 1)
    for prime in primes_till_square:
        prime_divisor = floor((x / prime)) * prime if x > prime else prime
        if prime_divisor == x and prime_divisor != prime:
            numbers[0] = False
        for num in range(prime_divisor + prime, y + 1, prime):
            numbers[num - x] = False
    if x == 1:
        numbers[0] = False
    primes = []
    for num in numbers:
        if num:
            primes.append(x)
        x = x + 1
    return primes


for i in range(int(input())):
    val = input().split(" ")
    for primes_in_range in get_primes_in_range(int(val[0]), int(val[1])):
        print(primes_in_range)
    print()
