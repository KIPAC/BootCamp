# Install Miniconda Python

Python at KIPAC can be a bit tricky, but the steps below, using [miniconda](http://conda.pydata.org/miniconda.html), should result in a generally useful setup. 


## Setup

1.  (Optional) If you're academic user, request an academic license here [on this page](https://store.continuum.io/cshop/academicanaconda). 
    You should receive an email with a license file, which you'll put it under `~/.continuum`.
   
2.  Go to [miniconda website](http://conda.pydata.org/miniconda.html) to download the correct version you need. Start the installation process by running:
    
    ``` 
    bash Miniconda-latest-Linux-x86_64.sh
    ```
    
    Follow the installation instruction.
   
3.  Append the following line to your `~/.bashrc` or `~/.cshrc` file.
   
    ```
    # If using bash
    export PATH="$HOME/miniconda/bin:$PATH"
 
    # If using (t)csh
    setenv PATH "$HOME/miniconda/bin:$PATH"
    ```
   
    Once this is done, source your `~/.bashrc` or `~/.cshrc`:
   
    ```
    source ~/.bashrc

    ### OR ###
    
    source ~/.cshrc  
    ```
 
4.  Make sure the installation is sucessful by check your python executable path:

    ```
    which python
    ```
  
5.  Update conda and install additional packages. Here's an example:
    
    ```
    conda update conda
    conda update --all
    conda install numpy scipy matplotlib ipython jupyter pandas astropy scikit-learn
    conda install mkl  # (only if you did Step 1)
    ```
   
6.  Some additional packages need to be install via `pip`, for example:
    
    ```
    pip install healpy
    ```
   
7.  Clean up some tarball files to save disk space:
     
    ```
    conda clean -t
    ```
     
8.  You're good to go!

