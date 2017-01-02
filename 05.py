#/usr/bin/python

# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
#  from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of
#  the numbers from 1 to 20?

def divByAll( n, top ):
  for test in xrange( top, 1, -1 ):
    if n % test != 0:
      return False
  return True

def smallestMultiple( n ):
  test = n
  while True:
    if divByAll( test, n ):
      return test
    test += n # has to be a factor of n

# main
print smallestMultiple( 20 )

