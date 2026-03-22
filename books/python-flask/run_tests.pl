use strict;
use warnings;
use feature 'say';
use Cwd;


my $folder = "src/examples/flask";
opendir my $dh, $folder or die;
my @folders = grep {$_ ne "." and $_ ne ".." and not -f "$folder/$_"} readdir $dh;
close $dh;

my $root = Cwd::cwd();
#say $root;
my $counter = 0;
my $total = @folders;
for my $dir (@folders) {
    # no tests
    next if $dir eq 'api_paremeters_required';
    next if $dir eq 'simple_auth';
    next if $dir eq 'hello-in-module';
    next if $dir eq 'login';
    next if $dir eq '50';
    next if $dir eq 'api_paremeters';
    next if $dir eq 'path-int';

    say $dir;

    chdir "$folder/$dir";
    my $exit_code = system "pytest";
    chdir $root;
    die "Test failed in $folder/$dir . $counter of $total examples passed." if $exit_code;
    $counter++;
}
