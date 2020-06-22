# Setting up a jupyter server on a remote computer using an ssh tunnel.

These instruction will help you run a jupyter server on a remote
machine (say one at SLAC or Stanford that has the data you want to use
on it), and connect to it from a local machine (i.e., your personal
computer).

This is going to require doing things on both machines.  You will need
a terminal to connect to the remote machine.  You will also use the
ssh protocol to connect the two machines.

- Before you start, you will need to pick:
  - A pair of id numbers to set up the connection, for example 8888
  and 8889.
   - You need to pick different numbers that other people using the
   same computer, so don't pick those.
- A password to use to connect to the server you run on the remote
machine.
  - This is *not* the same as your login password for that machine.

- On your local machine, one time only:
   - copy the jupnote file from this area to an area where you keep
   useful scripts
   
   cp BootCamp/docs/jupnote ~/bin/jupnote

   - edit the 'localid' and 'remoteid' lines in that file to match the
     number you picked.  For notes on using text editor see
     [here](text_editors.md).
    
   vim ~/bin/jupnote
   
    - make that file 'executable'
    
    chmod +x ~/bin/jupnote

- On the remote machine
  - Connect to the remote machine
  
    ssh -YK username@centos7.slac.stanford.edu
    
    - If you logged into a distributed machine, such as
      centos7, you should take note of which node you actually connected
      to (e.g., cent7a, cent7b..)
      
  - Invoke any setup scripts you need to access an enviroment with jupyter

    lsst_setup
    
  - Move to the directory you want to run the notebook server from

    cd lsst_jup_home/software/BootCamp/Python

  - Setup the password for the notebook

    jupyter notebook password
    
  - Start the notebook server
  
    jupyter notebook --no-browser --port=8889

- Back on your local machine, every time
  - run the jupnote command, using the node that you started the
    server on as an argument

    jupnote cent7d
  - point your web browser this address (use your own localid instead
    of 8888) http://localhost:8888/






