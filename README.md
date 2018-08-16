# EPIC Orientation

Repo for all orientation training materials

## Installation and set up instructions for orientation sessions

### Git

##### Download and Install Software

We will be using the command-line interface to [Git](https://www.git-scm.com/). Download is available at the link for those who do not already have the software installed. Once installed, Windows users should look for Git Bash, Mac and Linux will now have git embedded in a terminal.

If you are unfamiliar with the command-line, I found these notes helpful:

"A command-line is just an interface to your computer, totally analogous to the Finder or Windows Explorer, except that it’s text-based. As the name implies, you interact with it through “commands” — each line of input begins with a command and might have zero or more arguments, separated by spaces. The command-line keeps track of what directory (folder) you’re in, which is important to many of the commands you might be running."

Common commands include ```cd, pwd, ls, mkdir```. Please familiarize yourself with these commands before starting to use git. These [lecture notes](https://ocw.mit.edu/ans7870/6/6.005/s16/getting-started/#terminal) that are also linked at the bottom of this section have nice descriptions of these commands.

##### Create a Github

For the purposes of the git session and the data project, we will be hosting all code repositories on [Github](https://github.com/). Please create an account before orientation starts. I use my personal email for Github because I'd like my repositories to follow me throughout my whole life and not disappear into the void when an academic account expires. Feel free to play around with a repository on here if you are unfamiliar with any git at all and or unfamiliar with command-line as a whole.

##### Configure Git

There are many ways to make git a little more user friendly. I'll go through and detail how I configured my own git setup. Because every git commit needs to include both a name and e-mail, you can configure this on your local machine to automatically attach it to every commit you make. Don't worry if you don't quite understand what I'm saying, just type these into either Git Bash or Terminal, replacing in quotes with your personal information. Use the email address you used to set up your github account. 
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

These installation and setup instructions were copied liberally from these [lecture notes](https://ocw.mit.edu/ans7870/6/6.005/s16/getting-started/#terminal). I would highly recommend perusing these notes (skipping all the Java install stuff) but at least the last bit about the git workflow and playing around with a repository on [Github](https://github.com/)

### Python

##### Download Anaconda

Because Python is an open-source software, you will find yourself needing to use many packages. There are many package managers available but I would recommend [Anaconda](https://www.anaconda.com/download) since that is what SCC uses. 

##### Use Anaconda to install Python

Using Anaconda you can install Python 2.7 on your local machine. I prefer 2.7 because it makes dealing with legacy code a little easier but many people use find using the most up to date version of Python (no version number would be needed in the install command) works for them. Navigate to the command line and type:

```
conda install python=2.7
```

##### Install packages

Using Anaconda, install a few packages we will be using during the orientation session by running the following code in command-line. Note that the "-c" prefixes which channel of conda you can install from. It only needs to be specified if the channel is not anaconda.
```
conda install pandas
conda install numpy
conda install -c conda-forge selenium
conda install chromedriver
```

##### Text editor

Python comes with IDLE which is a text editor but is not the best in my opinion. Many RAs prefer [Sublime](https://www.sublimetext.com/) as a text editor for most languages.

### R

##### Download R

Here is the [link](https://cran.rstudio.com/) to download R

##### Setup RStudio

Many R users have a personal preference for [RStudio](https://www.rstudio.com/products/rstudio/download/). You can download using the link or navigate to anaconda by typing ```anaconda-navigator``` on your command-line and installing straight from there.

##### Install packages for R

Navigate to your command-line and type:
```
Rscript -e 'install.packages(c("tidyverse", "lfe", "sf"), repos = "https://cran.rstudio.com/")'
```

