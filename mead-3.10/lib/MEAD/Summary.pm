package MEAD::Summary;

require Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(write_summary);

use strict;

sub write_summary {
    my $summary = shift;
    my $destination = shift || \*STDOUT;

    unless (ref $destination) {
	unless (open TEMP, ">$destination") {
	    die "Unable to open $destination for writing.\n";
	}
	$destination = \*TEMP;
    }

    foreach my $order (sort {$a <=> $b} (keys %{$summary})) {
        my $sentref = $$summary{$order};
        print $destination "[$order]  $$sentref{'TEXT'}\n";
    }
}

