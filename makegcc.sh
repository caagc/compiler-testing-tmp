d1=default
d2=extreme
d3=guided
d4=enhanced
d5=combined
v1="gcc-4.3.0"
v2="gcc-4.4.0"
v3="gcc-4.5.0"
v4="gcc-4.6.0"
WORKDIR=/data/zzx/compiler_testing
version=$v4
configs=()

if [[ ! -d $version ]]; then
wget https://mirrors-i.tuna.tsinghua.edu.cn/sourceware/gcc/releases/$version/$version.tar.gz
tar xvf $version.tar.gz

for config in "${configs[@]}"
do
rm -r $version-$config
cp -r $version $version-$config
cp ./patches/gengtype.c $version-$config/gcc
done

for config in "${configs[@]}"
do
cd $WORKDIR/$version-$config/
rm -r build
mkdir build
./contrib/download_prerequisites
cd build
../configure --disable-bootstrap --enable-languages=c --enable-coverage --disable-multilib --prefix=$WORKDIR/$version-$config/build --disable-nls
make -j10 
if [[ $? != 0 ]]; then exit 1; fi
make install
cp $WORKDIR/scripts/cal.sh $WORKDIR/$version-$config/build/gcc
echo "cd $WORKDIR/$version-$config/build/gcc" >> $WORKDIR/$version-$config/build/gcc/cal.sh
echo "cal | grep executed | tail -n 1" >> $WORKDIR/$version-$config/build/gcc/cal.sh
cp $WORKDIR/scripts/reset.sh $WORKDIR/$version-$config/build/gcc
done

