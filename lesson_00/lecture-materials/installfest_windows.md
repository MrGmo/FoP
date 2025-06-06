# Windows Installfest

## What we'll cover
We are going to install everything that you will need for this course. Please do this in order!

1. Visual Studio Code & `code`
2. Understanding the Unix Environment
3. apt-get
4. Python

## VSCode with `code`
- Download and install [Visual Studio Code](https://code.visualstudio.com/download)
- During install, VSCode will add itself to your system's PATH envirnmental variable. This will allow you to open VSCode from the terminal by simply typing `code`. You can also open files in VSCode from the terminal by typing `code SOME_FILENAME`.

## Ubuntu / Bash
Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install), which installs Ubuntu within your Windows machine as a [virtual machine](https://www.vmware.com/topics/glossary/content/virtual-machine.html) (VM). Every time we do any sort of development in this class, you'll be accessing that VM and running Linux commands. 

To get to the bash shell, open Visual Studio Code, click on `Terminal -> New Terminal` and type `bash` when the terminal shows up at the bottom. You'll notice that the colors change and a new prompt will show up:
```sh
your_username@your_computer_name: ~$
```
At this point, you are able to run all the commands like the students on a Mac/Linux machine. To exit from the bash shell, type `exit`. You'll see the regular Powershell prompt. To enter the bash shell again, type `bash`.

## Installing Python/NPM/Node/Git
- The setup from here is the same as the students using a Linux machine. Complete the installfest instructions starting at [Advanced Package Tools](./installfest_ubuntu.md#advanced-package-tool)
