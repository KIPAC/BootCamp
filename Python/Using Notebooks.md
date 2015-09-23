# Using Notebooks

## Try Jupyter Notebooks on the cloud

Open your browser and visit [this website](https://try.jupyter.org/).


## Start a notebook running on your local machine

Open a terminal and run

```
jupyter-notebook
```

This will fire up your browser and point you to the running notebook server.

Note: if you have an older version of ipython (<= 3.x), replace `jupyter-notebook` with `ipython-notebook`.


## Start a notebook running on a remote machine

This generally involves two steps: (1) start a notebook instance on the remote machine and (2) set up a tunnel so you can connect to the remote notebook instance. Here's the breakdown:

1.  Open a terminal and `ssh` to the remote machine. Go to the directory where you want to start the notebook instance, and run

    ```
    # On a remote machine 
    jupyter-notebook --no-browser 
    ```

    Do not terminate this connection. You should see a message reading "The IPython Notebook is running at: http://localhost:8889/". Take note of the port number in this message (which is "8889" in this example). 

2.  Open another terminal on your local machine (Windows users, see below), and run

    ```
    # On your local machine
    ssh -N -L 8887:localhost:8889 <user>@<remote server>
    ```
    
    The remote server needs to be the same machine as in Step 1, and the second number (after "localhost") also needs to be the same number as the one you saw in Step 1. 

    Open your browser and connet to http://localhost:8887/

    (If you use Windows, find the option "Port Forwarding" in SecureCRT or "SSH Tunnel" in PuTTY. You need to set up a local port forwarding from port 8887 to localhost:8889.)


### Is there a simpler way?

    You can combine the two steps into one:

    ```
    ssh -t -L 8887:localhost:12345 <user>@<server> "jupyter-notebook --no-browser --notebook-dir=<your notebook dir> --port-retries=0 --port=12345"
    ```

    You may want to change the number "12345" to something else if you are not the only person using the remote machine. (Note that this number appears twice in the above command.)

    Another choice is to run the notebook instance at a public-facing address, so that the second step can be omitted. However, you **MUST** secure your connection to the remote instance with SSL and also use password to protect your notebook. The instruction can be found [here](http://ipython.org/ipython-doc/3/notebook/public_server.html). 

    
## Notebook Extensions

You can find some useful extensions in this [repository](https://github.com/ipython-contrib/IPython-notebook-extensions).

