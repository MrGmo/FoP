# Unix Terminal Basics

[Back to Week 1 Setup](https://github.com/ptbravoplatoon/curriculum/tree/master/Module-1--Javascript-and-Python-Fundamentals/wk-01--Setup)

> **READ FIRST**: Anything below using `< >` in the **Usage** sections is meant to be a placeholder value. Example: `<folder name>` you would not type this you would replace that entire placeholder with an actual folder name on your system.

**Keep in mind**: Most terminal commands are performing their task relative to where your terminal "thinks" its at directory-wise. Typing `pwd` will always tell you what "current working directory" your terminal is sitting at. If you `mkdir` a folder or `touch` a file it will be placed relatively to your "current working directory".

`pwd` - Print Working Directory
> Usage: `pwd`

`whoami` - Show the current user I am
> Usage: whoami

`ls` - List computer files (directory contents dont include hidden)
`ls -a` - List computer files and show hidden files
> **Usage**: `ls` -- alone will show the current directory contents
> **Usage**: `ls -a <folder name>` -- `-a` flag will allow us to see hidden files too
> **NOTE**: the contents of a directory there are always 2 special "folders".
> `.` - represents the CURRENT directory you used ls on
> `..` - represents the PARENT directory of the directory you used ls on

`cd` - Change directory
> **Usage**: `cd <folder name>`

`mkdir` - Make/Create a directory
> **Usage**: `mkdir <folder name>`

`rm` - Remove a file by filenames
> **Usage**: `rm <filename>`

`touch` - Creates a new empty file.
> **Usage**: `touch <filename>`

`cat` - Display contents of a file in the terminal.
> **Usage**: `cat <filename>`

`echo` - Prints to the console
> **Usage**: `echo <value>`

