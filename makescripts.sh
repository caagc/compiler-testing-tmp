d1=default
d2=extreme
d3=guided
d4=enhanced
d5=combined
scripts=($d1 $d4 $d5)
GCC=gcc-4.5.0
WORKDIR=/data/zzx/compiler_testing
for script in "${scripts[@]}"
do
testdir=compiler-testing-$script-$GCC
rm -r $testdir
mkdir $testdir
mkdir $testdir/data
mkdir $testdir/data/bugs
mkdir $testdir/data/c_files
touch $testdir/config_tuning.py
echo "GCC_PATH='$WORKDIR/$GCC-$script'" >> $testdir/config_tuning.py
cat scripts/config_tuning.py >> $testdir/config_tuning.py
echo "" >> $testdir/config_tuning.py
echo "Fuzzing$script()" >> $testdir/config_tuning.py
touch $testdir/generate.pl
echo "my \$GCC_PATH = \"$WORKDIR/$GCC-$script\";" >> $testdir/generate.pl
cat scripts/generate.pl >> $testdir/generate.pl
cp scripts/run.sh $testdir
done