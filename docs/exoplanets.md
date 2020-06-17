# Installing Anaconda and Jupyter on GPICruncher

Once you have an account on gpicruncher, which can be obtained by contacting Jeff Wade (jrw@stanford.edu), setting up anaconda and a jupyter notebook server is straightforward. The first step is to download the installer, which can be done from the terminal with wget. (Here the link is to the Python3 Linux 64-bit installer)

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
Make the script executable

    chmod +x Miniconda3-latest-Linux-x86_64.sh
    
And run it.

    ./Miniconda3-latest-Linux-x86_64.sh

You must agree to license terms, and for convenience I would have the installer run conda init for you. All that should be left is to 

    source .bashrc

And you should be able to run the conda command, in addition to seeing the appended (base) in front of the terminal prompt. This means that you are currently running the base environment in the package manager, in which we will want to install only essential packages.

    conda install jupyter numpy scipy matplotlib nb_conda_kernels

In general it is a good idea to learn how to [manage environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for running different software packages. Nb_conda_kernels allows you to modify which environment a script is being run in, from inside the jupyter notebook, which is very convenient when working with multiple environments.

Jupyter offers the ability to remotely edit and run scripts in a nice interactive interface, with inline plotting, and saved variables, eliminating the need for slow VNCs or buggy X-window interfaces. The jupyter notebook server by default creates a webserver which can only be accessed by the localhost (user on the machine) so we configure it with some options for remote access

    jupyter notebook --no-browser --port=12345

In general it is a good idea to pick a unique port number. Once the server is up and running, it should generate a login token for you in the terminal, which you should save. 

On your local machine, we need to create an SSH tunnel to the port which the server was just generated on, to access it remotely. This can be done with the following command
    
    ssh -f -N -L localhost:12345:localhost:12345 [username]@gpicruncher.stanford.edu

And the notebook server can now be accessed through the tunnel in your web browser.
(http://localhost:12345/)

Other Useful packages:

jupyter-lab (for the nice UI)

astropy (for reading .fits files and other astronomical things)

pandas (for tabulated data)

pygrib (for .grb files)

pyfftw (Fastest Fourier Transform in the West)

pytorch (gpu computing)
