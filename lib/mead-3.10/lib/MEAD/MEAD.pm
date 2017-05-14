package MEAD::MEAD;

require Exporter;
@ISA = qw(Exporter);
@EXPORT = qw($VERSION
	     $MEADDIR

	     $DEBUG
	     $VERBOSE

	     Debug);

use strict;

use vars '$VERSION';

use vars '$MEADDIR';

use vars '$DEBUG';
use vars '$VERBOSE';

#
# TODO: AJW 9/19
# read .meadrc files.
#

$VERSION = "3.07";

# NOTE: this is the ONLY place where the path to MEAD should be hardcoded.

#$MEADDIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/lib/mead-3.10";
$MEADDIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/lib/mead-3.10";

# I don't know what we're going to use these for.
$DEBUG = 0;
$VERBOSE = 0;

sub Debug {
    my $message = shift;
    my $crit = shift || 1;
    my $caller = shift;

    return unless $VERBOSE + $crit > 2;

    my $crit_str;
 
    if (!($caller)) { $caller = "(unknown)" }
    if (!($message)) { $message = "(none given)" }
    if (!($crit) || ($crit !~ /^[0-9]$/)) { $crit = 1 }
        
    if ($crit < 2) { $crit_str = "DEBUG" }
    elsif ($crit == 2) { $crit_str = "ERROR" }
    else { $crit_str = "FATAL" }

    if ($VERBOSE + $crit > 2) {
        print STDERR $crit_str.": ". $message;
        if ($VERBOSE > 1) {
            print STDERR " (in function: $caller)";
        }
        print STDERR "\n";
    }
}

1;
