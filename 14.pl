#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

=pod

multi-line comment

=cut

my $verbose = 0;
my $debug = 0;
my $max_seq = 1000;

GetOptions(
  "verbose" => \$verbose,
  "debug" => \$debug,
  "maxseq=i" => \$max_seq
);

my %tracker = ( 1 => 1 );

sub sequence {
  my $n = shift( @_ );
  print $n if $debug;
  my $count = 1;
  my $cur = $n;

  while( $cur > 1 ) {
    if( exists $tracker{$cur} ) {
      $count += $tracker{$cur} - 1;
      print " -> ... (+" . ($tracker{$cur} - 1) . ") " if $debug;
      last;
    }

    if( $cur % 2 == 0 ) {
      $cur /= 2;
    } else {
      $cur = ( 3 * $cur ) + 1;
    }
    print " -> $cur" if $debug;

    ++$count;
  }

  print "= [$count]\n" if $debug;
  $tracker{$n} = $count;
  return $count;
}

my $max = 1;
my $maxStart = 0;
for( my $i = 1; $i < $max_seq; $i++ ) {
  my $terms = sequence( $i );
  print "sequence($i) = $terms" if $verbose;

  if( $terms > $max )
  {
    $max = $terms;
    $maxStart = $i;
    print " *" if $verbose;
  }
  print "\n" if $verbose;
}

print "Max: sequence($maxStart) yielded $max terms\n";
#print Dumper( \%tracker ) . "\n" if $debug;

