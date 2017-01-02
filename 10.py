#/usr/bin/python
import math

'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def isPrime( n ):
  if n < 2:
    return False

  # test for 2, 3, and 5 as a basecase
  if n == 2 or n == 3 or n == 5:
    return True

  if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False

  # ...now from 7 to sqrt(n), skipping even numbers
  for test in xrange( 7, int( math.sqrt(n) ) + 1, 2 ):
    if n % test == 0:
      return False

  return True

sum = 0
for i in range(1, 2000000):
  if isPrime( i ):
    sum += i

print sum
