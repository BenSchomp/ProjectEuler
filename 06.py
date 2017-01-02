#/usr/bin/python

# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is:
#   1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first
#  ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first
#  one hundred natural numbers and the square of the sum.


def sumOfSquares( a, b ):
  sum = 0
  for i in xrange( a, b+1 ):
    sum += i * i

  return sum

def squareOfSums( a, b ):
  sum = 0
  for i in xrange( a, b+1 ):
    sum += i

  return sum * sum

def differenceOfSumOfSquares( a, b ):
  return squareOfSums( a, b ) - sumOfSquares( a, b )

# main
print differenceOfSumOfSquares( 1, 100 )

