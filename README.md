# EPIC Orientation

Repo for all orientation training materials

## Installation and set up instructions for orientation sessions

### Git

##### Download and Install Software

We will be using the command-line interface to [Git](https://www.git-scm.com/). Download is available at the link for those who do not already have the software installed. Once installed, Windows users should look for Git Bash, Mac and Linux will now have git embedded in Terminal. Navigate to either Git Bash or Terminal to run all command-line prompts.

If you are unfamiliar with the command-line, I found these notes helpful:

"A command-line is just an interface to your computer, totally analogous to the Finder or Windows Explorer, except that it’s text-based. As the name implies, you interact with it through “commands” — each line of input begins with a command and might have zero or more arguments, separated by spaces. The command-line keeps track of what directory (folder) you’re in, which is important to many of the commands you might be running."

Common commands include ```cd, pwd, ls, mkdir```. Please familiarize yourself with these commands before starting to use git. These [lecture notes](https://ocw.mit.edu/ans7870/6/6.005/s16/getting-started/#terminal) that are also linked at the bottom of this section have nice descriptions of these commands.

##### Create a Github

For the purposes of the git session and the data project, we will be hosting all code repositories on [Github](https://github.com/). Please create an account before orientation starts. I use my personal email for Github because I'd like my repositories to follow me throughout my whole life and not disappear into the void when an academic account expires. Feel free to play around with a repository on here if you are unfamiliar with any git at all and or unfamiliar with command-line as a whole.

##### Configure Git

There are many ways to make git a little more user friendly. I'll go through and detail how I configured my own git setup. Because every git commit needs to include both a name and e-mail, you can configure this on your local machine to automatically attach it to every commit you make. Don't worry if you don't quite understand what I'm saying, just run these commands in either Git Bash or Terminal, replacing in quotes with your personal information. Use the email address you used to set up your github account. 
``` 
git config --global user.name "Your Name"
git config --global user.email "username@gmail.com"
```
I also like using colors when I interact with git because it makes the command-line experience much less painful so I would also recommend running the following commands on the command-line
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

Using Anaconda you can install Python 2.7 on your local machine. I prefer 2.7 because it makes dealing with legacy code a little easier but many people find using the most up to date version of Python (no version number would be needed in the install command) works for them. Navigate to the command-line and run:

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

##### Set Up RStudio

Many R users have a personal preference for [RStudio](https://www.rstudio.com/products/rstudio/download/). You can download using the link or navigate to anaconda by running ```anaconda-navigator``` on your command-line and installing straight from there.

##### Install packages for R

Navigate to your command-line and run:
```
Rscript -e 'install.packages(c("tidyverse", "lfe", "sf", "ggplot2"), repos = "https://cran.rstudio.com/")'
```

### LaTeX

The LaTeX tutorial itself will be done using Overleaf but software installation is still required to compile pdfs on your local machine. These are just some preferred software from RAs who frequently use LaTeX.

##### Mac OS 

If you have a Mac, a preferred LaTeX software is [TeXShop](https://pages.uoregon.edu/koch/texshop/). 

##### Windows

If you're on a Windows machine, a preferred LaTeX software is [TexMaker](http://www.xm1math.net/texmaker/) which also runs on Mac.

### Stata

You all already have Stata on your machines (if you don't please talk to one of us ASAP). For the data project you will need to install a few user-written packages, some by our very own Andrew Smith!

Unfortunately, Stata does not integrate well with the command-line so navigate to your Stata command prompt and copy/paste the following in there in one block.

```
* Install ftools (remove program if it existed previously)
cap ado uninstall ftools
net install ftools, from("https://raw.githubusercontent.com/sergiocorreia/ftools/master/src/")

* Install reghdfe 4.x
cap ado uninstall reghdfe
net install reghdfe, from("https://raw.githubusercontent.com/sergiocorreia/reghdfe/master/src/")

* Install boottest for Stata 11 and 12
if (c(version)<13) cap ado uninstall boottest
if (c(version)<13) ssc install boottest

* Install moremata (sometimes used by ftools but not needed for reghdfe)
cap ssc install moremata

* Install ivreg2, the core package
ssc install ivreg2

* Finally, install this package
cap ado uninstall ivreg2hdfe
cap ado uninstall ivreghdfe
net install ivreghdfe, from(https://raw.githubusercontent.com/sergiocorreia/ivreghdfe/master/src/)

* Install estout/esttab
ssc install estout, replace

* For the balance table
cap ado uninstall "bcheck"
net install bcheck, from("https://raw.githubusercontent.com/jandrewsmith03/bcheck/master/")

* For simplerd
cap ado uninstall "simplerd"
net install simplerd, from("https://raw.githubusercontent.com/jandrewsmith03/simplerd/master/")

* For some extension to egen
ssc install egenmore
```


