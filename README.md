# EPIC Orientation

Repo for all orientation training materials

## Installation and set up instructions for orientation sessions

### Git

##### Download and Install Software

We will be using the command-line interface to [Git](https://www.git-scm.com/). Download is available at the link for those who do not already have the software installed. Once installed, Windowsusers should look for Git Bash, Mac and Linux will now have git embedded in a terminal.

If you are unfamiliar with the command-line, I found these notes helpful:

"A command-line is just an interface to your computer, totally analogous to the Finder or Windows Explorer, except that it’s text-based. As the name implies, you interact with it through “commands” — each line of input begins with a command and might have zero or more arguments, separated by spaces. The command-line keeps track of what directory (folder) you’re in, which is important to many of the commands you might be running."

Common commands include ```cd, pwd, ls, mkdir```. Please familiarize yourself with these commands before starting to use git. These [lecture notes](https://ocw.mit.edu/ans7870/6/6.005/s16/getting-started/#terminal) that are also linked at the bottom of this page have nice descriptions of these commands.

##### Configure Git

There are many ways to make git a little more user friendly. I'll go through and detail how I configured my own git setup. Because every git commit needs to include both a name and e-mail, you can configure this on your local machine to automatically attach it to every commit you make. Don't worry if you don't quite understand what I'm saying, just type these into either Git Bash or Terminal, replacing in quotes with your personal information. Use the email address you would like to set up your github account with. I use my personal email for this because I'd like my github repositories to follow me throughout my whole life and not disappear into the void when an academic account expires.
``` 
git config --global user.name "Your Name"
git config --global user.email "username@gmail.com"
```
I also enjoy using colors when I interact with git because it makes the command line experience much less painful so I would also recommend running the following commands on the command-line
```
git config --global color.branch auto
git config --global color.diff auto
git config --global color.interactive auto
git config --global color.status auto
git config --global color.grep auto
```
The command ```git log``` basically allows you to view the history of your repository. There is a way to make this more human readable so I create the alias ```git lol``` by running the following command.
```
git config --global alias.lol "log --graph --oneline --decorate --color --all"
``` 

These installation and setup instructions were copied liberally from these [lecture notes](https://ocw.mit.edu/ans7870/6/6.005/s16/getting-started/#terminal)