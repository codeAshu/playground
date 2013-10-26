""" This program will print first x numbers of prime No"""

def XprimeNo(x):
   n=x
   primes_total = 0;
   confirmed_primes = [];
   confirmed_primes.append(1);
   while len( confirmed_primes) <x:
           possible_primes = range(0,n);

           for current_number in range(2,n):
              if possible_primes[current_number] != False:  #if they are not false than they are prime nos
                 confirmed_primes.append(possible_primes[current_number]);

                 if len( confirmed_primes) ==x:
                     break

              increments = current_number;
              while (increments < n):
                    possible_primes[increments] = False;  #here multiple of all numbers are set to false
                    increments = increments + current_number;
           n+=100 

   return confirmed_primes

import time
ts = time.time()
print XprimeNo(10000)
print len(XprimeNo(10000))
print "run Time ="  +str( time.time() - ts)
