# https://drive.google.com/file/d/1q9yXrxRo3W62OJzo7F43QfgjXhr0FiY7/view?usp=share_link
# https://github.com/RehanSaeed/Bash-Cheat-Sheet
# https://www.educative.io/blog/bash-shell-command-cheat-sheet
# https://www.educative.io/blog/bash-shell-command-cheat-sheet

# ls - List directory contents
"""
ls command allows you to quickly view all files within the specified directory.

Syntax: ls [option(s)] [file(s)]
Common options:
-a      Include directory entries whose names begin with a dot (.) [Basicaly hidden files]
-l      List files in the long format.        
"""

# echo — Prints text to the terminal window
"""
echo output
"""

# touch — Creates a file
"""
touch filename
"""

# mkdir — Create a directory
"""
mkdir directry_name
"""

# grep — search
"""
grep is used to search text for patterns specified by the user. It is one of the most useful and powerful commands. There are often scenarios where you'll be tasked to find a particular string or pattern within a file, but you don't know where to start looking, that is where grep is extremely useful.

Syntax: grep [option(s)] pattern [file(s)]

Common options: -i, -c, -n

Tutorial: https://youtu.be/Iqmx6CYYZTk
"""

# man — Print manual or get help for a command
"""
man command
"""

# pwd — Print working directory

# cd — Change directory
"""
cd directory
"""

# mv — Move or rename directory
"""
mv is used to move or rename directories. Without this command, you would have to individually rename each file which is tedious. mv allows you to do batch file renaming which can save you loads of time.

Syntax: mv [option(s)] argument(s)
"""

# rmdir — Remove directory
"""
rmdir will remove empty directories. This can help clean up space on your computer and keep files and folders organized. It’s important to note that there are two ways to remove directories: rm and rmdir. The distinction between the two is that rmdir will only delete empty directories, whereas rm will remove directories and files regardless if they contain data or not.

Syntax: rmdir [option(s)] directory_names
"""

# locate — Locate a specific file or directory
"""
This is by far the simplest way to find a file or directory. You can keep your search broad if you don’t know what exactly it is you’re looking for, or you can narrow the scope by using wildcards or regular expressions.

Syntax: locate filename(s)
"""

# less — view the contents of a text file
"""
The less command allows you to view files without opening an editor. It's faster to use, and there's no chance of you inadvertently modifying the file.

Syntax: less file_name
"""

# > — redirect stdout
"""
The > character is the redirect operator. This takes the output from the preceding command that you’d normally see in the terminal and sends it to a file that you give it. As an example, take echo “contents of file1” > file1. Here it creates a file called file1 and puts the echoed string into it.

Syntax: >
"""

# cat — Read a file, create a file, and concatenate files
"""
cat is one of the more versatile commands and serves three main functions: displaying them, combining copies of them, and creating new ones.

Syntax: cat [option(s)] [file_name(s)] [-] [file_name(s)]
"""

# | — Pipe
"""
A pipe takes the standard output of one command and passes it as the input to another.

Syntax: |

Tutorial: https://youtu.be/3hbqDtfI3zE
"""

# head — Read the start of a file
"""
By default, the head command displays the first 10 lines of a file. There are times when you may need to quickly look at a few lines in a file and head allows you to do that. A typical example of when you'd want to use head is when you need to analyze logs or text files that change frequently.

Syntax: head [option(s)] file(s)
"""

# tail — Read the end of a file
"""
By default, the tail command displays the last 10 lines of a file. There are times when you may need to quickly look at a few lines in a file and tail allows you to do that. A typical example of when you'd want to use tail is when you need to analyze logs or text files that change frequently.

Syntax: tail [option(s)] file_names
"""

# chmod — Sets the file permissions flag on a file or folder
"""
There are situations that you'll come across where you or a colleague will try to upload a file or modify a document and you receive an error because you don't have access. The quick fix for this is to use chmod. Permissions can be set with either alphanumeric characters (u, g, o) and can be assigned their access with w, r, x. Conversely, you can also use octal numbers (0-7) to change the permissions. For example, chmod 777 my_file will give access to everyone.

Syntax: chmod [option(s)] permissions file_name
"""

# exit — Exit out of a directory
"""
The exit command will close a terminal window, end the execution of a shell script, or log you out of an SSH remote access session.

Syntax: exit
"""

# history — list your most recent commands
"""
An important command when you need to quickly identify past commands that you’ve used.

Syntax: history
"""

# clear — Clear your terminal window
"""
This command is used to clear all previous commands and output from consoles and terminal windows. This keeps your terminal clean and removes the clutter so you can focus on subsequent commands and their output.

Syntax: clear
"""

# cp — copy files and directories
"""
Use this command when you need to back up your files.

Syntax: cp [option(s)] current_name new_name
"""

# kill — terminate stalled processes
"""
The kill command allows you to terminate a process from the command line. You do this by providing the process ID (PID) of the process to kill. To find the PID, you can use the ps command accompanied by options -aux.

Syntax: kill [signal or option(s)] PID(s)
"""

# sleep — delay a process for a specified amount of time
"""
sleep is a common command for controlling jobs and is mainly used in shell scripts. You’ll notice in the syntax that there is a suffix; the suffix is used to specify the unit of time whether it be s (seconds), m (minutes), or d (days). The default unit of time is seconds unless specified.

Syntax: sleep number [suffix]
"""

################## TOP NETWORKING COMMANDS ###############################
# https://www.educba.com/networking-commands/
"""
1. ping
2. netstat
3. ipconfig
4. hostname
5. tracert
6. nslookup
7. route
8. arp
9. path ping
"""