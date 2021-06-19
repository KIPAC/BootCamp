# Setting up a Linux computer to use for research

There are a number of common Linux distributions and it would be difficult to cover all of them here.
In general, these will be based off of Debian, Red Hat, or Arch, the primary difference (for these purposes) being the package manager of each respective distribution—APT, DNF, and pacman, respectively.

## Basic tools

You will need some way to manage files, connect to SLAC computers and
open display windows.  Generally that will be a combination of using
terminal windows and an X-windows systems for graphics.

### Terminal

Each Linux distribution typically comes with a terminal emulator via their desktop environment; e.g., most installations of Ubuntu and Fedora use the [GNOME](https://www.gnome.org/) desktop environment which includes the [GNOME Terminal](https://help.gnome.org/users/gnome-terminal/stable/).

For a comprehensive list of terminal emulators in Linux, see the [ArchWiki](https://wiki.archlinux.org/title/List_of_applications#Terminal_emulators).

### X Windows system (X-Quartz)

The X Windows system is a very common way to open connections to and send graphics from processes running on remote computers.
While some Linux distributions are moving towards [Wayland](https://wayland.freedesktop.org/), many scientific applications rely on X to render graphics.
If X is not already installed on your system via, e.g., [Xorg](https://www.x.org/wiki/), it is recommended that you do so.
If you are using Wayland, compatability is available through [XWayland](https://wayland.freedesktop.org/xserver.html); see the [ArchWiki](https://wiki.archlinux.org/title/Wayland#XWayland).


### Text editor

Any distribution of Linux will typically come with a text editor (if not just `vi` or even `ed`).
For a comprehensive list of text editors on Linux, see the [ArchWiki](https://wiki.archlinux.org/title/List_of_applications#Text_editors).

Consider [Text Editors](text_editors.md) for a brief overview of some of the more common text editors.

## Other Tools

The tools that you are most likely to need on your personal computer
in order to do research "git", which is a file versioning system and
"conda", which is a combination of python and a software package management system.

### git

git is a versioning system that is pretty ubiquitous in our
work.  It lets many users work together to manage a large set of
files.  This can be set of software, or a paper draft, or some
documentation, or pretty much any kind of files. 

See the [ArchWiki](https://wiki.archlinux.org/title/Git) for an overview.

[Documentation](https://xkcd.com/1597)

Run the following command to "clone" this repository from GitHub onto your computer:

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

You can download anaconda from here:

[anaconda](https://docs.anaconda.com/anaconda/install/linux/)

I recommend installing anaconda under your home directory '~/Applications/'

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
