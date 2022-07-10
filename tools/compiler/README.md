## GCC

Example dirtycow compiling:

`gcc -pthread exploit.c -o exploit`

```
-pthread
           Define additional macros required for using the POSIX threads
           library.  You should use this option consistently for both
           compilation and linking.  This option is supported on
           GNU/Linux targets, most other Unix derivatives, and also on
           x86 Cygwin and MinGW targets.
```
