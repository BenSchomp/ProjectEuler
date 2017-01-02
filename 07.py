#/usr/bin/python
import math

# 10001st prime
# Problem 7
#
# By listing the first six prime numbers:
#  2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10001st prime number?

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

def nthPrime( n ):
  i = 0
  count = 0

  while count < n:
    i += 1
    if isPrime( i ):
      count += 1
      #print str(count) + ": " + str(i)
    
  return i

# main
print nthPrime( 10001 )




