#"What is the value of the first triangle number to have over five hundred divisors?"

""" It will print all the prime nos less than x """

def primesUnderX(x):
   possible_primes = range(0,x);

   primes_total = 0;
   confirmed_primes = [];
   confirmed_primes.append(1);

   for current_number in range(2,x):
      if possible_primes[current_number] != False:
         confirmed_primes.append(possible_primes[current_number]);

         increments = current_number;
         while (increments < x):
            possible_primes[increments] = False;
            increments = increments + current_number;
            
   return confirmed_primes

###################################################################

""" Take each exponant of prime factor and increase it by one and multipy them it will give the no of factrors/divisors"""
""" 30 = 2^1 * 3^1 * 5^1
so prime factor exponant are 1,1,1  ,
total no of factors are (1+1)*(1+1)*(1+1) = 8
30 = 1,2,3,5,6,10,15,30
"""
def findFactors(number, primes):
   original_number = number;
   times_repeated = 0;
   total_factors = 1;
   current_prime = 1;

   while  (number > 1):

      while (number % primes[current_prime] == 0):
         times_repeated += 1;
         number = number/primes[current_prime];

      total_factors *= (times_repeated + 1);
      times_repeated = 0;

      current_prime += 1;

   return total_factors;
###################################################################
tri_numbers = [0];
current_number = 1;

primes = primesUnderX(100);

"""
while (findFactors(tri_numbers[current_number-1], primes) < 5):
   tri_numbers.append( tri_numbers[current_number - 1] + current_number);
   current_number = current_number + 1;
"""
print primes
