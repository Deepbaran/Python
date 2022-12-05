# https://youtu.be/e7BufAVwDiM
"""
1. Hello Bash Scripting
2. Redirect to file
3. Comments
4. Conditional Statements
5. Loops
6. Script input
7. Scritp output
8. Pipes
9. Strings processing
10. Numbers and Arithmetic
11. Declare Command
12. Arrays
13. Functions
14. Files and Directories
15. Sending email via script
16. Curl in Script
17. Professional menus
18. Wait for filesystem events with inotify
19. Introduction to grep
20. Introduction to awk
21. Introduction to sed
22. Debugging Bash Scripts
"""

# https://drive.google.com/file/d/1q9yXrxRo3W62OJzo7F43QfgjXhr0FiY7/view?usp=share_link
"""
command [OPTION]... [ARGUMENT]...

Short options : -
Long options: --

$ ls -la --human-readable Flask

Files - Some kind of data specially in a special format
Directories - Places where Files are stored
Links - These are references to either a file or a directory, i.e. they don't contain data, but just point to another place in the filesystem.
Filesystems in any UNIX system are usually structured as rooted trees. The root of the filesystem is designated by the slash '/'. 
"""

"""
=================
FILE SYSTEM:
=================
$ pwd
 /d/Upskilling/01 - Existing Skills/08 - Python
It gives the current working directory
There two kinds of paths.
Absolute - Paths that start from the root
Relative - Paths that start from the current working directory

------------------
$ ls
 Advanced/  Basics/  Flask/  README.md  Tools/
list down contents in the current working directory directiory

$ ls Flask
 01-myflaskapp/   02-FlaskRestAPI/  'commans&Tools.txt'   schemas.sql
list down contents of a particular directory. We can pass Relative and absolute both paths.

=================
HELP UTILITIES:
=================
$ man ls
Provides manual for the ls command.
SPACE - Scroll down
Q - exit

-k | --apropos List the programs whose name or short description match the key-
word you searched for. Note that this is the same thing the apropos program

does.6
-a | --all Show all man pages from all sections which match the keyword you searched
for.

------------------
$ sudo apt install texinfo-doc-nonfree
To get these in debian, save them using the above command and then use the below command to get the same as man.

$ info ls

------------------
> Get-Help ls -online
For UNIX systems like windows use this command to see the manuals online.

------------------
$ ls --help / ls -h
Use this command to get a quick glimpse on what the command does rather than reading the whole manual.

------------------
$ help cd
Use help to get the helping manual for shell builtins.

------------------
$ type COMMAND_NAME
use this to check if it is a program or shel builtin. For example:

$ type cd
cd is a shell builtin

------------------
'which' tells you where in the filesystem the executable you are going to call is located
and if you have installed two versions each of them will reside in a different place.

$ which pwd
/usr/bin/pwd
which tells you that if you call the pwd program, it will use the one in the /bin directory.
So, in case you have a second version of pwd installed, which resides in /usr/local/bin,
you'll have to use the absolute path to call it.

------------------
$ whereis COMMAND
 pwd: /usr/bin/pwd /usr/include/pwd.h
this will show you where versions of COMMAND are installed, where their man pages
are located and if the source code of the command is stored in a standard location on
the system.

The actual difference between which and whereis
is that the former looks through your PATH variable and returns the first executable it
finds which actually is the one your shell would execute while the latter scans through
your whole PATH as well as MANPATH plus some standard locations commonly used for
programs on any (GNU/)Linux system, and returns everything it finds there, separated
into executables, source files, and man pages.

------------------
$ whatis ls
 ls (1) - list directory contents
This command tells us what a command does on the most basic level.




"""