#!/usr/bin/perl
use strict;
use warnings;

my $n = 15;

my $exp = 2**$n;
print $exp,"\n";

my $sum = 0;
while( $exp > 0 )
{
  my $tmp = $exp;
  $exp /= 10;
  print "$tmp $exp\n";
}
print $sum, "\n";

