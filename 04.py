#!/usr/bin/python 

# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome
#  made from the product of two 2-digit numbers is 9009 = 91 x 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPal( n ):
  s = str( n )
  l = len( s )

  for i in xrange( 0, (l / 2) ):
    if s[i] != s[l-i-1]:
      return False

  return True

# main
largest = 0
for a in xrange( 100, 1000 ):
  for b in xrange( 100, 1000 ):
    test = a * b
    if test > largest and isPal( test ):
      largest = test

print largest

