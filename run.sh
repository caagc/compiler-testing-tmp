d1=default
d2=extreme
d3=guided
d4=enhanced
scripts=($d3)
GCC=gcc-4.6.0
WORKDIR=/data/zzx/compiler_testing
for script in "${scripts[@]}"
do
testdir=compiler-testing-$script-$GCC
cd $WORKDIR/$testdir
bash run.sh
done
