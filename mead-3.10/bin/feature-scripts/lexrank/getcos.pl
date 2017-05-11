#!/usr/bin/perl

use lib("/clair4/projects/mead307/source/mead/lib");

use MEAD::SimRoutines;

# some vars for the MEAD routines
our $lang ="ENG";
our $idffile = "enidf";

@lines = <>;

foreach $l (@lines) {
    $i = 0;
    foreach $m (@lines) {
        if ($i < $j) {
	  $cosine = GetLexSim ($l,$m);
	  print "$i $j $cosine\n";
	  print "$j $i $cosine\n";
	}
	$i++;
    }
    $j++;
}

__END__
