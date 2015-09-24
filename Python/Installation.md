# Install Miniconda Python

Python at KIPAC can be a bit tricky, but the steps below, using [miniconda](http://conda.pydata.org/miniconda.html), should result in a generally useful setup. 


## Setup

1.  (Optional) If you're academic user, request an academic license here [on this page](https://store.continuum.io/cshop/academicanaconda). 
    You should receive an email with a license file, which you'll put it under `~/.continuum`.
   
2.  Go to [miniconda website](http://conda.pydata.org/miniconda.html) to download the correct version you need. 
    If you are installing miniconda in the linux/unix machine (like on the remote server), you can start the installation process by running:
    
    ``` 
    bash Miniconda-latest-Linux-x86_64.sh
    ```
    
    Follow the installation instruction.
   
3.  Open a text editor to append the following line to your `~/.bashrc`, `~/.bash_profile`, or `~/.cshrc` file.
   
    ```
    # If using bash
    export PATH="$HOME/miniconda/bin:$PATH"
 
    # If using (t)csh
    setenv PATH "$HOME/miniconda/bin:$PATH"
    ```
    
    If you are on a remote server and do not know how to edit a text file, you can run (for the csh case):

    ```
    cp ~/.cshrc ~/.cshrc.bak
    echo 'setenv PATH "$HOME/miniconda/bin:$PATH"' >> ~/.cshrc
    ```
    
    Once this is done, source your `~/.bashrc`, `~/.bash_profile`, or `~/.cshrc`. For example:
   
    ```
    source ~/.bashrc
    ```
 
4.  Make sure the installation is sucessful by check your python executable path:

    ```
    which python
    ```
    You should see miniconda in the output.
  
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


