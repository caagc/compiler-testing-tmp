cal() {
	directories=()
    for dir in */; do
        directories+=("$dir")
    done
    directories+=("$PWD"/)
    for dir in "${directories[@]}"; do
        gcov -f -o "$dir" "$dir"*.gcda 2>&1
    done
}
#cd /data/zzx/gcc-4.6.0-default/build/gcc
#cal | grep "executed" | tail -n 1
