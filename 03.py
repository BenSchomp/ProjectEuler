#!/usr/bin/python 
import math

# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

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

# previously this returned a list of the prime factors
#  of which the largest one is the answer ... but that
#  took considerable amount of time ... so just print them
#  out as you find them and the last one displayed is the
#  largest ... so far. :)
def largestPrimeFactor( n ):
  largest = 1
  x = 2
  while True:
    if n % x == 0 and isPrime( x ):
      print x
      largest = x

    x += 1
    if x > ( n / 2 ):
      break
  
  return largest

def test_isPrime():
  for x in xrange( 2, 100 ):
    if isPrime( x ):
      print str(x) + " is prime!"

#print largestPrimeFactor( 13195 )
print largestPrimeFactor( 600851475143 )

