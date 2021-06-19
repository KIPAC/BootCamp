# Setting up a Chrome OS computer to use for research

## Basic tools

You will need some way to manage files, connect to SLAC computers and
open display windows.  Generally that will be a combination of using
terminal windows and an X-windows systems for graphics.

## Crostini

### Linux

To setup Linux on a Chromebook, follow the instructions [here](https://chromeos.dev/en/linux/setup).
Note that this Linux container is based off of [Debian](https://www.debian.org/), a Linux distribution that is the basis for other distributions including Ubuntu.

This Linux container includes a [Terminal](https://chromeos.dev/en/productivity/terminal) and includes support for the X Window System.

### Text editor

You are going to need some way to edit files.

There are many different options, here is a summary of some of your choices:

[Text Editors](text_editors.md)

The Linux shell should already have 'vim' installed and accessible from within a Linux shell terminal; you can verify by typing

`which vim`

which should print: 

`/usr/bin/vim`

If you wish to use `emacs` instead, I recommend you install via your Linux terminal:

`sudo apt-get emacs`


## Other Tools

The tools that you are most likely to need on your personal computer
in order to do research "git", which is a file versioning system and
"conda", which is a combination of python and a software package management system.

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

We haven't had time to verify this, but it sounds like you want to use `/usr/local/anaconda3` as the installation path.
This may be different under Crostini.


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

Note that you will want the Linux version for compatability with the Linux container.

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
