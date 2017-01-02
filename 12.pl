#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

=pod

Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the
natural numbers. So the 7th triangle number would be:
  1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over
 five divisors.

What is the value of the first triangle number to have over
 five hundred divisors?

=cut

my $TARGET_DIVISORS = 500;
my $divs = 0;


sub factor {
  my @factors;
  my $n = shift( @_ );

  push @factors, 1;
  if( $n < 2 )
  { return @factors; }

  for( my $i = 2; $i <= $n / 2; $i = $i + 1 ) {
    if( $n % $i == 0 ) {
      my $q = $n / $i;

      $divs++;
      push @factors, $i;
    }
  }
  push @factors, $n;
  return @factors;
}

sub factorHash {
  my $n = shift( @_ );

  my %factors = (
    1 => $n,
    $n => 1 
  );

  if( $n < 2 ) {
    return \%factors;
  }

  for( my $i = 2; $i <= $n / 2; $i = $i + 1 ) {
    if(  exists $factors{$i} )
    { next; }

    if( $n % $i == 0 ) {
      my $q = $n / $i;

      $divs++;
      $factors{$i} = $q;
      $factors{$q} = $i;
    }
  }

  return \%factors;
}

sub triangle {
  my $cur = 1;
  my $i = 1;

  while( 1 ) {
    my @factors = factor( $cur );
    my $numDivisors = @factors;
    #print "$cur: " . join( ", ", @factors ) . " -- [$numDivisors]\n";
    if( $numDivisors > $TARGET_DIVISORS )
    { return $cur; }
    ++$i;
    $cur = $cur + $i;
  }
}

sub triangle2 {
  my $cur = 1;
  my $i = 1;

  while( 1 ) {
    my $factors = factorHash( $cur );
    my $numDivisors = keys %$factors;
    #print "$cur: " . Dumper($factors) . " -- [$numDivisors]\n";
    if( $numDivisors > $TARGET_DIVISORS )
    { return $cur; }
    ++$i;
    $cur = $cur + $i;
  }
}

print "** CURRENTLY WILL MAX OUT CPU AT 2+ HOURS **\n";
#print triangle() . " ($divs divisions)\n";
$divs = 0;
print triangle2() . " ($divs divisions)\n";
