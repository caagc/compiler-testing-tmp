use File::stat;

my $CSMITH_HOME = $ENV{"CSMITH_HOME"}; 
my $HEADER = "-I$CSMITH_HOME/runtime";

my $CSMITH_TIMEOUT = 120; # 2 minutes 
my $COMPILER_TIMEOUT = 120;# 2 minutes
my $PROG_TIMEOUT = 10;
my $MIN_PROGRAM_SIZE = 500;

my @OPT = ("-O0", "-O1", "-O2", "-Os", "-O3");
my @COMPILERS;
my $COMPILE_OPTIONS = "";

# csmith configuration, csmith cnt, program state, c file
my $c_file_path = "./data/c_files";
my $bug_file_path = "./data/bugs";
my $state_path = "./state.txt";
my $coverage_path = "./coverage.txt";
my $csmith_cnt_tmp_file = "./csmith_cnt_tmp.txt";
my $csmith_timeout_file = "./data/csmith_err.txt";
my $csmith_total_bug_cnt_file = "./data/csmith_total_bug_cnt.txt";
my $total_bug_cnt;
my $nargs = scalar(@ARGV);
my $csmith_config_file = $ARGV[0];
my $csmith_cnt_output_file = $ARGV[1];
my $c_file_cnt = $ARGV[2];

sub read_value_from_file($$) {
    my ($fn, $match) = @_;
    open INF, "<$fn" or die;
    while (my $line = <INF>) {
        $line =~ s/\r?\n?$//;            # get rid of LF/CR 
        if ($line =~ /$match/) {
            close INF;
            return $1;
        }     
    }
    close INF;
    return "";
}

sub read_2_value_from_file($$) {
    my ($fn, $match) = @_;
    open INF, "<$fn" or die;
    while (my $line = <INF>) {
        $line =~ s/\r?\n?$//;            # get rid of LF/CR 
        if ($line =~ /$match/) {
            close INF;
            return ($1, $2);
        }     
    }
    close INF;
    return ("", "");
}

sub runit ($$$) {
    my ($cmd, $timeout, $out) = @_; 
    my $res;
	$res = system "timeout $timeout $cmd > $out 2>&1";
    my $success = 0; 
    if ($? == -1) {
        print "can't execute $cmd\n";
    }
    elsif ($? & 127) {
        print "died while executing $cmd\n";
    }
    elsif ($res == -1) {
        print "can't execute $cmd\n";
    }
    else {
        $success = 1;
    }
    my $exit_value  = $? >> 8;
    if ($exit_value == 124) {
        print "hangs while executing $cmd\n";
        $success = 0;
    }
    return ($success, $exit_value);
}

sub write_desc_to_file($$$) {
    my ($desc, $hasbug, $testfile) = @_;
    open OUT, ">>$state_path" or die "cannot write to $state_path\n";
    print OUT "$desc\n";
    close OUT;
    if ($hasbug == 1) {
        system "cp $testfile $bug_file_path/test$total_bug_cnt.c";
        open OUT, ">>$bug_file_path/test$total_bug_cnt.c" or die "cannot write to $bug_file_path/test$total_bug_cnt.c\n";
        print OUT "/* $desc */\n/*";
        system "cat $csmith_config_file >> $bug_file_path/test$total_bug_cnt.c";
        system "cat $csmith_cnt_tmp_file >> $bug_file_path/test$total_bug_cnt.c";
        $total_bug_cnt++;
        print OUT "*/\n";
        close OUT;
    }
}

sub compile_and_run($$$$) {
    my ($compiler, $test_file, $exe, $out) = @_; 
    my $command = "$compiler $test_file $COMPILE_OPTIONS $HEADER -o $exe";  
    # compile random program
    my ($res, $exit_value) = runit($command, $COMPILER_TIMEOUT,  "compiler.out"); 
    # print "after run compiler: $res, $exit_value\n";
    if (($res == 0) || (!(-e $exe))) {
        # exit code 124 means time out
        return ($exit_value == 124 ? 2 : 1);         
    }

    # run random program 
    ($res, $exit_value) = runit("./$exe", $PROG_TIMEOUT, $out);
    if (($res == 0) || (!(-e $out))) {
        # exit code 124 means time out
        return ($exit_value == 124 ? 4 : 3);      
    }
    return 0;
}

sub run_compilers($) {
    # length of OPT
    (my $test_cnt) = @_;
    my @checksums;
    my @tested_compilers; 
    my $interesting = 0;
    my $opt_len = scalar(@OPT);
    my $test_file = "$c_file_path/test$test_cnt.c";

    for (my $i = 0; $i < $opt_len; $i++) {
        my $compiler = "$GCC_PATH/build/bin/gcc $OPT[$i]";
        my $exe = "$c_file_path/test$test_cnt.out$i";
        my $out = "$c_file_path/test$test_cnt.log$i";
        my $res = compile_and_run($compiler, $test_file, $exe, $out);

        if ($res) {
            if ($res == 1) { 
                write_desc_to_file("Crash: compiler crashed with $compiler $COMPILE_OPTIONS!", 1, $test_file); 
                $interesting = 1;
                last;
            }
            elsif ($res == 2) {
                write_desc_to_file("Hang: compiler hangs with $compiler $COMPILE_OPTIONS!", 1, $test_file); 
                $interesting = 1;
                last;
            }
            elsif ($res == 3) { 
                write_desc_to_file("Crash: random program crashed!", 1, $test_file); 
                # random program crashes, a likely wrong-code bug, but
                # can't rule out the probablity of a Csmith bug
                $interesting = -2;     
                last;
            } else {
                # write_bug_desc_to_file("Hang: random program hangs!"); 
                    # program hangs, not interesting
                $interesting = -1;    
                    last;
            }
        }
        else {
            die "cannot find $out.\n" if (!(-e $out));
            my $sum = read_value_from_file($out, "checksum = (.*)");
            $interesting = 2 if (scalar(@checksums) > 0 && $sum ne $checksums[0]); 
            push @checksums, $sum;
            push @tested_compilers, "$compiler $COMPILE_OPTIONS";
        }             
    }
    if ($interesting == 2) { 
        write_desc_to_file ("Wrongcode: Found checksum difference between compiler implementations", 1, $test_file); 
    }
    if ($interesting  == 0) {
        write_desc_to_file ("Correct: No checksum difference between compiler implementations", 0, $test_file); 
    }
    system "rm -f $c_file_path/test$test_cnt.out* $c_file_path/test$test_cnt.log* test*.obj compiler.out csmith.out";
    return $interesting;
}

sub get_coverage_inc() {
    my $coverage = 0;
    if (-e $coverage_path) {
        $coverage = read_value_from_file($coverage_path, "coverage = (.*)");
    }
    system "bash $GCC_PATH/build/gcc/cal.sh > $coverage_path";
    (my $percent,$lines) = read_2_value_from_file($coverage_path, "Lines executed:(.*)% of (.*)");
    my $new_coverage = $percent * $lines / 100;
    print("$coverage, $new_coverage\n");
    my $coverage_inc = int($new_coverage - $coverage);
    print("coverageInc = $coverage_inc\n");
    open OUT, "> $coverage_path" or die "cannot write to $coverage_path\n";
    print OUT "coverage = $new_coverage\n";
    print OUT "coverageInc = $coverage_inc\n";
    close OUT;
    exit 0;
}

sub test_one ($) {
    (my $n) = @_;
    my $cfile = "test$n.c";
    my $seed;
    my $filesize;


    # while(1) {
    system "timeout $CSMITH_TIMEOUT $CSMITH_HOME/build/bin/csmith --feature-file $csmith_cnt_tmp_file --probability-configuration $csmith_config_file --output $c_file_path/$cfile";
        # $filesize = stat("$c_file_path/$cfile")->size;
        # print "$cfile is $filesize bytes\n";
        # last if ($filesize >= $MIN_PROGRAM_SIZE);
    # }
    my $exit_value  = $? >> 8;
    if ($exit_value == 124) {
        print "csmith hangs while executing\n";
        system "cat $csmith_config_file >> $csmith_timeout_file";
        return -7;
    }
    return run_compilers($n);
}

# if state_path exist
if (-e $state_path) {
    system "rm $state_path";
}

# if csmith_cnt_output_file exist
if (-e $csmith_cnt_output_file) {
    system "rm $csmith_cnt_output_file";
}

if (-e $csmith_cnt_tmp_file) {
    system "rm $csmith_cnt_tmp_file";
}

if (! -e $csmith_total_bug_cnt_file) {
    open OUT, ">$csmith_total_bug_cnt_file" or die "cannot write to $csmith_total_bug_cnt_file\n";
    print OUT "1";
    close OUT;
}

open IN, "<$csmith_total_bug_cnt_file" or die "cannot read from $csmith_total_bug_cnt_file\n";
$total_bug_cnt = <IN>;
print "total_bug_cnt: $total_bug_cnt\n";
close IN;

my $i = 0;
while ($i < $c_file_cnt) {
    my $res = test_one ($i);
    if ($res != -1) {
        if ($res == -7) {
            last;
        }
        system "cat $csmith_cnt_tmp_file >> $csmith_cnt_output_file";
	    $i++;
    } 
} 

open OUT, ">$csmith_total_bug_cnt_file" or die "cannot write to $csmith_total_bug_cnt_file\n";
print OUT "$total_bug_cnt";
close OUT;

get_coverage_inc();