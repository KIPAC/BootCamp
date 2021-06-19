# Setting up a Windows 10 computer to use for research

## Basic tools

You will need some way to manage files, connect to SLAC computers and
open display windows.  Generally that will be a combination of using
terminal windows and an X-windows systems for graphics.

### Terminal and Environment

There are two primary approaches you can take here:
- Do everything "natively" in Windows—this may be more straightforward, but may be a bit more difficult as you get to more advanced topics.
- Use the Windows Subsystem for Linux—this takes a bit more work to setup, but will give you a development environment more similar to what is often used in labs (i.e., unix-based, as opposed to Windows).

Both of these options are valid, but using the Windows Subsystem for Linux may make it easier to follow documentation in the future.

#### Windows Terminal

As of Build 2020, Microsoft has released [Windows Terminal 1.0](https://devblogs.microsoft.com/commandline/windows-terminal-1-0/), which can be installed from the [Microsoft Store](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab).
Windows Terminal includes many modern terminal emulator features and is generally recommened over `cmd.exe`.

#### Windows Subsystem for Linux

As of Windows 10 build 14328 (released in 2016), it is now possible to set up a
Unix-like terminal on Windows, using the following guide:

[Linux Shell on Windows 10](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)

You can choose from a number of Linux systems, though Ubuntu is recommended, unless you have previous experience
with a specific Linux system.

Following these instructions will set-up a Linux system within your Windows laptop. A few notes regarding this:
* Your Linux home directory will be: `/home/<your_linux_username>`. 
* Since you have a Linux system, installation of new programs should be done following Linux installation
  instructions and using the Linux terminal tools such as `apt-get`.
* Your Windows files will be located at: `/mnt/c/Users/<your_windows_username>/`. Here you can find your usual "Documents",
  "Pictures", "Downloads", etc. folders you should be familiar with.


### X Windows system (VcXsrv Windows X Server)

The X Windows system is a very common way to open connections to and send graphics from processes running on remote computers.   It is generically useful and
we recommend you install it if you are using a windows laptop.

[VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/)

Download and run the installer to install VcXsrv. You will need to make sure the installed VcXsrv application is running to use the window
forwarding features; if you shut down/restart your computer, you will need to restart the application.


### Text editor

You are going to need some way to edit files.   I strongly recommend
that you do not use Notepad, WordPad, or other built-in Windows editors to try and edit software files.

There are many different options, here is a summary of some of your
choices:

[Text Editors](text_editors.md)

The Windows 10 Linux shell should already have 'vim' installed and accessible from within a Linux shell terminal; you can verify by typing

`which vim`

which should print: 

`/usr/bin/vim`

If you wish to use `emacs` instead, I recommend you install via your Linux terminal:

`sudo apt-get emacs`


## Other Tools

The tools that you are most likely to need on your personal computer
in order to do research "git", which is a file versioning system and
"conda", which is a combination of python and a software package management system.

Note that the following documentation assumes you are using the Linux shell via the Windows Subsystem for Linux.

### git

git is a versioning system that is pretty ubiquitous in our
work.  It lets many users work together to manage a large set of
files.  This can be set of software, or a paper draft, or some
documentation, or pretty much any kind of files. 

I recommend using the instructions under using "Installing Git on Ubuntu" on the page below:

[Installation](https://phoenixnap.com/kb/how-to-install-git-on-ubuntu)

[Documentation](https://xkcd.com/1597)

Running the following command in a terminal window will setup git and
use it to "clone" this Bootcamp:

    # Install git using apt-get
    sudo apt-get update
    sudo apt-get install git
    # "Clone" this repository into a directory called "BootCamp"
    git clone https://github.com/KIPAC/BootCamp.git


(The lines that start with '#' are comments.)
   

### Anaconda or Miniconda and Jupyter Notebooks

conda is a combination of python and a software package management
system.   You can either install the full anaconda package or your can
install miniconda, a minimal installer that bootstraps itself and only installs the package you need.

Note that the full anaconda distribution comes with a lot of tutorials
and extra things, so you might want to install that version.


#### Anaconda

You can download the Linux version of anaconda from here:

[anaconda](https://docs.anaconda.com/anaconda/install/linux/)

I recommend installing anaconda under your home directory '~/Applications/' or whevever is equivalent on your distribution.



##### Setting up anaconda for in a terminal window 

Once you have installed anaconda you can also set up your terminal
windows to activate conda for that terminal by doing this:

    # Activate conda
    . ~/Applications/anaconda3/etc/profile.d/conda.sh
    # "Activate" the "base" conda environment
	conda activate

(The lines that start with '#' are comments.)


#### Miniconda

You can download miniconda from there, (make sure to get the python 3 version):

[minconda](https://docs.conda.io/en/latest/miniconda.html)

If you go the route of installing miniconda there are a number of packages, such as jupyter notebooks that you will likely need to install.

Running the following commands in a terminal window will install a minimal set of packages to
let you run jupyter notebooks locally. 

    # Activate conda, if you ran conda init when you installed
    # miniconda you don't need to do this
    . /Users/echarles/miniconda3/etc/profile.d/conda.sh 
    # Create a conda environment to work these examples
    conda create --name kipac python
    # Install the stuff you need (from the conda-forge software 'channel')
    conda install --name kipac -c conda-forge numpy scipy jupyter
    # "Activate" the kipac environment
	conda activate kipac

(The lines that start with '#' are comments.)

Alternatively, you can run

    conda env create -f kipac-env.yaml
	conda activate kipac

to create and activate an environment named `kipac` that has been prepared in advance.

Note that you will need to run

    conda activate kipac

each time you begin a new session (i.e., open a terminal).

### Set Up Jupyter Notebook

You will need to perform a few extra steps to get Jupyter to use your favorite web browser when displaying notebooks.

You need to define a BROWSER variable. To do this open up `~/.bashrc` using your text editor and add the following line:

    export BROWSER="/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"

If you are using a different web browser than Chrome (example above) you will need to modify the path to point to the appropriate
executable.

Next enter the following commands:

     jupyter notebook --generate-config
     echo c.NotebookApp.use_redirect_file = False >> ~/.jupyter/jupyter_notebook_config.py

You may need to close and restart your terminal for the changes to take effect.


### Running a notebook


If you want to start a notebook you can then do:

    # Start a notebook server in the current directory that you are in 
    jupyter notebook 

Once you have started a notebook server you will want to navigate to
the notebook that you want to run.  Let's start with the basic python
/ notebook tutorial.   In your browser you can selection that notebook
to open it.

BootCamp ->Python -> Python (1).ipynb

Note.   You can get you notebook browser to start up in
a different folder in a few different ways.   For example you could:

    # Version one, go to a directory and start the notebook server there
    cd ~/BootCamp/Python
	jupyter notebook
    # Version two, use the --notebook-dir option
    jupyter notebook --notebook-dir="BootCamp/Python"

<!--  LocalWords:  Miniconda Jupyter minconda kipac conda-forge numpy
 -->
<!--  LocalWords:  scipy
 -->
