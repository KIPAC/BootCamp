# Connect to servers with SSH

Here I use Stanford's server `cardinal` as an example. You can use the same procedure to connect to other servers, like the SLAC servers.

## If you are using Windows:

If you have an active SUNet ID, visit [this page](https://itservices.stanford.edu/service/ess/pc/securecrt) to download and install SecureCRT. Follow the instructions on [this page](https://itservices.stanford.edu/service/ess/pc/docs/securecrt) to connect to `cardinal.stanford.edu`. Use your SUNet ID to log in.

If you don't have an active SUNet ID, please download PuTTY from [this page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). You will need at least `putty.exe`.

In both, you can also download and install [VcXsrv](http://sourceforge.net/projects/vcxsrv/). This allows you to see the graphic interfaces when connecting to a server with SSH. We won't use it in this tutorial but it may come handy at a later time. 


## If you are using Mac OS (OS X):

Open a "terminal" (under Applications/Utilities, or just type "terminal" in Spotlight), and type

    ssh <your SUNet ID>@cardinal.stanford.edu

And enter your SUNet password to log in.


