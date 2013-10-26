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
