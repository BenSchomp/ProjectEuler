#/usr/bin/python
import math

'''
  Special Pythagorean triplet
  Problem 9

  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

  a^2 + b^2 = c^2
  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
  Find the product abc.
'''

def findTriplet( n ):
  a = 1
  b = 1
  c = 1

  n = 1000
  for a in xrange( 1, n + 1 ):
    for b in xrange( a + 1, n + 1 ):
      for c in xrange( b + 1, n + 1 ):
        if a + b + c != n:
          continue
        if (a * a) + (b * b) == (c * c):
          return a * b * c

  return 0

# main
print findTriplet( 1000 )
