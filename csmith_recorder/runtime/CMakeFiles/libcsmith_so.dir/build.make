# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /data/zzx/compiler_testing/csmith_recorder

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /data/zzx/compiler_testing/csmith_recorder

# Include any dependencies generated for this target.
include runtime/CMakeFiles/libcsmith_so.dir/depend.make

# Include the progress variables for this target.
include runtime/CMakeFiles/libcsmith_so.dir/progress.make

# Include the compile flags for this target's objects.
include runtime/CMakeFiles/libcsmith_so.dir/flags.make

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o: runtime/CMakeFiles/libcsmith_so.dir/flags.make
runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o: runtime/volatile_runtime.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/data/zzx/compiler_testing/csmith_recorder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o"
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o   -c /data/zzx/compiler_testing/csmith_recorder/runtime/volatile_runtime.c

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/libcsmith_so.dir/volatile_runtime.c.i"
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /data/zzx/compiler_testing/csmith_recorder/runtime/volatile_runtime.c > CMakeFiles/libcsmith_so.dir/volatile_runtime.c.i

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/libcsmith_so.dir/volatile_runtime.c.s"
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /data/zzx/compiler_testing/csmith_recorder/runtime/volatile_runtime.c -o CMakeFiles/libcsmith_so.dir/volatile_runtime.c.s

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.requires:

.PHONY : runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.requires

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.provides: runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.requires
	$(MAKE) -f runtime/CMakeFiles/libcsmith_so.dir/build.make runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.provides.build
.PHONY : runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.provides

runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.provides.build: runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o


# Object files for target libcsmith_so
libcsmith_so_OBJECTS = \
"CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o"

# External object files for target libcsmith_so
libcsmith_so_EXTERNAL_OBJECTS =

runtime/libcsmith.so.0.0.0: runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o
runtime/libcsmith.so.0.0.0: runtime/CMakeFiles/libcsmith_so.dir/build.make
runtime/libcsmith.so.0.0.0: runtime/CMakeFiles/libcsmith_so.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/data/zzx/compiler_testing/csmith_recorder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library libcsmith.so"
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libcsmith_so.dir/link.txt --verbose=$(VERBOSE)
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && $(CMAKE_COMMAND) -E cmake_symlink_library libcsmith.so.0.0.0 libcsmith.so.0 libcsmith.so

runtime/libcsmith.so.0: runtime/libcsmith.so.0.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate runtime/libcsmith.so.0

runtime/libcsmith.so: runtime/libcsmith.so.0.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate runtime/libcsmith.so

# Rule to build all files generated by this target.
runtime/CMakeFiles/libcsmith_so.dir/build: runtime/libcsmith.so

.PHONY : runtime/CMakeFiles/libcsmith_so.dir/build

runtime/CMakeFiles/libcsmith_so.dir/requires: runtime/CMakeFiles/libcsmith_so.dir/volatile_runtime.c.o.requires

.PHONY : runtime/CMakeFiles/libcsmith_so.dir/requires

runtime/CMakeFiles/libcsmith_so.dir/clean:
	cd /data/zzx/compiler_testing/csmith_recorder/runtime && $(CMAKE_COMMAND) -P CMakeFiles/libcsmith_so.dir/cmake_clean.cmake
.PHONY : runtime/CMakeFiles/libcsmith_so.dir/clean

runtime/CMakeFiles/libcsmith_so.dir/depend:
	cd /data/zzx/compiler_testing/csmith_recorder && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /data/zzx/compiler_testing/csmith_recorder /data/zzx/compiler_testing/csmith_recorder/runtime /data/zzx/compiler_testing/csmith_recorder /data/zzx/compiler_testing/csmith_recorder/runtime /data/zzx/compiler_testing/csmith_recorder/runtime/CMakeFiles/libcsmith_so.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : runtime/CMakeFiles/libcsmith_so.dir/depend

