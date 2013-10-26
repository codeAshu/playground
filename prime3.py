import math
primes = set([2])
value = 3
number = 1000
while value < math.sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print value
            number /= value
print number
