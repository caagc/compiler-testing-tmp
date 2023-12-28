testdir=`ls | grep compiler-testing`
newshot=`date +%d`_`date +%H%M%S`
echo $newshot
mkdir snapshots/$newshot
for dir in $testdir
do
newshotdir=snapshots/$newshot/$dir
mkdir $newshotdir
cp -r $dir/data/bugs $newshotdir
cp -r $dir/coverage_log.txt $newshotdir
cp $dir/list.txt $newshotdir
done