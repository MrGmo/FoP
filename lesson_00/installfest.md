FROM: Monday, October 3, 2022

REFACTOR ALL OF THIS WITH GITHUB LINK!


====================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)



### Computer Setup (Mac, Linux, & Windows)
Before we get started, just know that this will be chaos. Your goal is to get a working environment, not to understand everything that happens. Please follow along closely!
* [Slack](https://slack.com/downloads) - for all communication purposes
* [Zoom](https://zoom.us/support/download)
* Sign up for [Operation Code](https://operationcode.org/join)

### Mac Setup
* Make sure you have an Apple ID
* Download XCode from the Mac App Store
* Ensure that you're running the most recent operating system. You can check your version by going to "System Preferences" and clicking on "Software Update"
* [VSCode](https://code.visualstudio.com/download)
* [iTerm](https://www.iterm2.com/downloads.html)
* [Complete Installfest (MacOS)](./lecture-materials/installfest.md)

### Ubuntu/Mint Setup
* [Complete Installfest (Ubuntu/Mint Version)](./lecture-materials/installfest_ubuntu.md)

### Windows Setup
- Ensure that you're running the most recent operating system (Windows 10 and 11 are both fine). You can update to the latest Windows version by selecting `Start > Settings > **Windows Update **> Check for updates.`
- [Complete Installfest (Windows)](./lecture-materials/installfest_windows.md)

### Lecture Topics
* Your new Integrated Development Environment (IDE)
  * Your IDE is where you write, execute, and view your code in the browser. For us, we'll be using VSCode to write code, iTerm2 or VSCode Terminal to execute code, and Google Chrome as the browser.

* VSCode Settings / Extensions
  * Make these your settings under Code -> Preferences -> Settings in VSCode (or in settings.json):
  ```
  {
    "editor.fontSize": 14,
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.renderLineHighlight": "gutter",
    "editor.tabSize": 2,
    "editor.wordWrap": "on",
    "explorer.confirmDelete": false,
    "explorer.confirmDragAndDrop": false,
    "files.autoSave": "onFocusChange",
    "window.zoomLevel": 0,
    "workbench.colorTheme": "Visual Studio Dark",
    "workbench.iconTheme": "vscode-icons",
    "workbench.startupEditor": "newUntitledFile",
    "[python]": {
      "editor.insertSpaces": true,
      "editor.tabSize": 4
    },

  }
  ```
* Extensions are tools to make your job as a developer easier. Please install these:
  * Sublime Text Keymap and Settings Importer
  * Beautify
  * VSCode Icons
  * Bracket Pair Colorizer
  * Path IntelliSense
  * Preview on web server
  * Python
  * Live Share
  * Live Share Audio

* Unix Commands / The Command Line
  * A frequent flyer who travels to the same hotel chain over and over again will have his preferences known by the hotel so that whenever they arrive, they get a similar experience. The same applies to your terminal - you want the same settings each time you load it up. Run `code ~/.bash_profile` to customize your terminal (unless you have settings you like already):
  ```
  parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
  }

  if [ -f ~/.git-completion.bash ]; then
    . ~/.git-completion.bash
  fi

  export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$(parse_git_branch) \[\033[00m\]$\[\033[00m\] "
  export PROMPT_COMMAND='echo -ne "\033]0;${PWD##*/}\007"'
  export CLICOLOR=1
  export LSCOLORS=ExFxBxDxCxegedabagacad
  ```

### External Resources
* Sublime and Atom are two other text editors to edit code. They use the same keyboard shortcuts and save a lot of time when you're writing code. Luckily for us, the creators of VSCode have also accounted for these shortcuts in a package that we installed earlier.
  * Bookmark and use the [Shortcuts](https://www.shortcutfoo.com/app/dojos/sublime-text-3-mac/cheatsheet)
  * VSCode [Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
