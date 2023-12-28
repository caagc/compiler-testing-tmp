# Install script for directory: /data/zzx/compiler_testing/csmith_recorder/runtime

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/data/zzx/compiler_testing/csmith_recorder/build")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.a")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/lib" TYPE STATIC_LIBRARY FILES "/data/zzx/compiler_testing/csmith_recorder/runtime/libcsmith.a")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  foreach(file
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0.0.0"
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0"
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0.0.0;/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0;/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/lib" TYPE SHARED_LIBRARY FILES
    "/data/zzx/compiler_testing/csmith_recorder/runtime/libcsmith.so.0.0.0"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/libcsmith.so.0"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/libcsmith.so"
    )
  foreach(file
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0.0.0"
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so.0"
      "$ENV{DESTDIR}/data/zzx/compiler_testing/csmith_recorder/build/lib/libcsmith.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/csmith.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/csmith_minimal.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/custom_limits.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/custom_stdint_x86.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/platform_avr.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/platform_generic.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/platform_msp430.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/random_inc.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/safe_abbrev.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/stdint_avr.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/stdint_ia32.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/stdint_ia64.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/stdint_msp430.h;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/volatile_runtime.c;/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/volatile_runtime.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0" TYPE FILE FILES
    "/data/zzx/compiler_testing/csmith_recorder/runtime/csmith.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/csmith_minimal.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/custom_limits.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/custom_stdint_x86.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/platform_avr.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/platform_generic.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/platform_msp430.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/random_inc.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/safe_abbrev.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/stdint_avr.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/stdint_ia32.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/stdint_ia64.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/stdint_msp430.h"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/volatile_runtime.c"
    "/data/zzx/compiler_testing/csmith_recorder/runtime/volatile_runtime.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/safe_math.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0" TYPE FILE FILES "/data/zzx/compiler_testing/csmith_recorder/runtime/safe_math.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/safe_math_macros.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0" TYPE FILE FILES "/data/zzx/compiler_testing/csmith_recorder/runtime/safe_math_macros.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/safe_math_macros_notmp.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0" TYPE FILE FILES "/data/zzx/compiler_testing/csmith_recorder/runtime/safe_math_macros_notmp.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/windows/stdint.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/data/zzx/compiler_testing/csmith_recorder/build/include/csmith-2.3.0/windows" TYPE FILE FILES "/data/zzx/compiler_testing/csmith_recorder/runtime/windows/stdint.h")
endif()

