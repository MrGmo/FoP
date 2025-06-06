# CodePlatoon Installfest

## What we'll cover
We are going to install everything that you will need for this course. Please do this in order!

1. Visual Studio Code & `code`
2. Understanding the Unix Environment
3. apt-get
4. Python
5. NPM/Node
6. Git

## VSCode with `code`
- Download [Visual Studio Code](https://code.visualstudio.com/download) and click on the `.deb` installer.
- During install, VSCode will add itself to your system's PATH envirnmental variable. This will allow you to open VSCode from the terminal by simply typing `code`. You can also open files in VSCode from the terminal by typing `code SOME_FILENAME`.

## Advanced Package Tool
[Advanced Package Tool](https://en.wikipedia.org/wiki/APT_(software)) (APT) is a package manager for Ubuntu to handle the installation, versioning and removal of software. It comes installed on Ubuntu by default. Let's ensure that we're using the most updated/upgraded version:

**Updating and Upgrading**
The `update` command in apt will resynchronize your package index with their sources. This goes out to each software's source to check what updates are available. The update require's elevated permissions. Therefore you'll need to run the command using `sudo` (super user do). The command will require your user password. It's the same password you used to login to your system.
```sh
sudo apt-get update -y
```

Now that apt-get has an updated list of current software, you'll want to upgrade anything that requires upgrading

```sh
sudo apt-get upgrade -y
```

## Python
Python comes built in with Ubuntu but to ensure that we have the must up to date version, let's run the following commands:
```sh
sudo apt-get install python3
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-setuptools
```

## NPM and NodeJS
In this section, we'll use apt to install npm, a package manage for node.
We'll then use npm to install n, which manages different versions nodejs.
Lastly, we'll use n to install the latest stable version of nodejs.
```sh
sudo apt-get install npm
sudo npm install -g n
sudo n stable
```

## GIT

```sh
sudo apt-get install git -y
```

Next, we'll configure Git so that we can download/upload to Github easily:


Next, You'll want to get your gitconfig setup to recognize your github credentials:
1. Set up your command line Git [username](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git#setting-your-git-username-for-every-repository-on-your-computer)
2. Set up your command line Git user [email](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#setting-your-email-address-for-every-repository-on-your-computer)
3. Cache your Github [password](https://help.github.com/articles/caching-your-github-password-in-git/) so that you don't have to type it in every single time you push to Github.
  - If you are using Windows, simply use `git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager-core.exe"` at the command line for this step.

Finally, ensure that VSCode is your global text editor for all things Git:

```sh
git config --global core.editor "code -n -w"
```

Confirm `gitconfig` is set up, both for your username/email and gitignore by running `git config --global -l`
You should see that your username, email, gitignore, and editor are all listed.

## Updating your bash profile
We're going to set up your bash_profile which will run every time you open a new terminal. Think of it as commands run on terminal startup. And we'll use VSCode to set this up. From the terminal type:
```sh
code ~/.bash_profile
```

VSCode should open with the `.bash_profile` as the current document. If you didn't have a profile before, it'll be empty. If you did, paste the code below at the bottom of your profile:
```sh
alias python='python3'
alias pip='pip3'
```

These two aliases are used to disambiguate python versions on your system. Ubuntu comes with python 2.7 installed and we'll be using Python 3 in this course. The alias makes it so you can just type **python** to execute the "correct" version rather than typing **python3** every time.

These aliases won't automatically be applied in your current terminal, but they will take effect in any new terminal windows you open.  


