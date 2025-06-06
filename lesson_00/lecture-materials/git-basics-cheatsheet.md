# Git Basics Commands

[Back to Week 1 Setup](https://github.com/ptbravoplatoon/curriculum/tree/master/Module-1--Javascript-and-Python-Fundamentals/wk-01--Setup)

> **READ FIRST**: Anything below using `< >` in the usage is meant to be a placeholder value. Example: `<filename>` you would not type this you would replace that entire placeholder with an actual filename (or described item).

`git init` - Initializes a NEW Git repository. ONLY Do this command if you are creating a repo from scratch DO NOT use this command if you are Forking/Cloning an assignment from GitHub.

Usage: `git init`

`git status` - Show information about changes to files that have been made.

> Usage: `git status`

> **NOTE**: If RED files are listed they are considered "unstaged" if they are file changes you want to keep/finalize, you need to git add them.
>
> If GREEN files are listed they are considered "staged" files. Staged files are awaiting to be committed/finalized into the repo. You can stage multiple files.

`git add` - Add a file to the "staging" area to prepare it to be included with your eventual commit. Multiple files can be part of a single commit.

> Usage: `git add <filename>`

`git commit` - Commits are like "save points" for your files. This command will effectively save your change to the repo. But you should ALWAYS use the -m flag to include a message wrapped in double quotes to describe your changes. Be short/concise with your message.

> Usage: `git commit -m "<your message here>"`

`git log` - Show all git commits that have happened.

> Usage: `git log`

`git clone` - Will allow you to "clone" or copy down a repo from a GitHub hosted repository by providing a URL to a repo you have access to.

> Usage: `git clone <a URL goes here>`

`git push` - After commiting changes on your Local (your computer) copy you can "push up" your commit change to GitHub's copy of that same repo which doesnt yet have those changes.

> Usage: `git push origin master` -- this will push your changes to the master branch. This may change in the future when we talk about Branching from master.
