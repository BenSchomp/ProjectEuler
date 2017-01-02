#!/usr/bin/perl
use strict;
use warnings;

my $SIZE = 20;
my $count = 0;

sub nextStep {
  my ( $curX, $curY ) = @_;
  #print "[$curX,$curY] ";

  # Basecase, reached the bottom right
  if( $curX == $SIZE and $curY == $SIZE ) {
    $count++;
    #print "count: $count\n";
    return;
  }

  # Go Right
  if( $curX < $SIZE ) {
    nextStep( $curX + 1, $curY );
  }

  # Go Down (but only if northeast of the symmetry line)
  if( $curX > 0 and $curY < $SIZE ) {
    nextStep( $curX, $curY + 1 );
  }
}

nextStep( 0, 0 );  
print "** CURRENTLY WILL MAX OUT CPU **\n";
print "answer: ", $count * 2, "\n"; # for other side of symmetry, x2

