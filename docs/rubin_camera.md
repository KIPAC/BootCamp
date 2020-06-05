# Computing Environment for Vera Rubin Observyatory Camera Work

To analyze test data from the LSST camera you will need a set of
software tools known as the LSST Data Management (DM) stack, as well
as a few other tools.  These tools are largely set up for you in the 

## Jupyter Notebook Setup.


## Interactive shell setup.

Typically you will want to use the centos7 interactive cluster at
SLAC.  That cluster has access to the camera data and
the data analysis software.

See [this page](slac_computing.md) about setting up your computer to remotely 
log in to SLAC. 

Typically I do this by running this command from a terminal or xterm
window on Mac laptop.  

    $ ssh -tt -Y username@centos7.slac.stanford.edu

Note: the "$" represents the unix command prompt.

See [this page](windows_setup.md) for how to do that from windows.

One time only, edit the hidden configuration file '.bash_profile' in your home
directory to invoke the group configuration file.

You can invoke an editor like so (note: the "$" represents the unix
command prompt)::

    $ nano .bash_profile

You can find links to more information about various unix text editors
[here](text_editors.md)

You will want to add this line to your '.bash_profile' file.

    source /nfs/farm/g/lsst/u1/group_config/setup_dm_stack.bashrc

That will set you up with the same configuration the rest of the
camera data analysis group is using.

In particular that will define a command that sets the parts of the
LSST software enviroment that you will need.   You can invoke that
command like so:

    $ lsst_setup


At that point you can check that things are set up by asking the shell
which version of python is active:

    $ which python
    /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2020_01/python/miniconda3-4.7.10/envs/lsst-scipipe-4d7b902/bin/python


You can also make sure that your python enviroment is working by doing
something like this:  (note, in this case the python command prompt is "> > >"):

    $ python
    Python 3.7.2 (default, Dec 29 2018, 06:19:36) 
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    >>> import lsst
    >>> lsst.__file__
    '/cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2020_01/stack/miniconda3-4.7.10-4d7b902/Linux64/fgcmcal/19.0.0+17/python/lsst/__init__.py'

That just tells you where the LSST software is located.















