# Stanford Computing Accounts

## Stanford's Shared Computing Environment

Anyone with a SUNet ID should have access to Stanford's Linux computing resources, which can be accessed by `ssh` using your SUNet credentials and are documented [here](https://uit.stanford.edu/service/sharedcomputing). These include nodes for
* low-intensity computing such as email (_cardinal.stanford.edu_)
* general interactive computing, including most analysis with runtimes <1 day (_rice.stanford.edu_)
* non-interactive high-performance computing (_wheat.stanford.edu_, _oat.stanford.edu_)

(updated 2020-06-12)

## Sherlock Cluster (high-performance computing)

Free computing, easy to access, good for jobs needing ~10-100(ish) cores. Anyone with an SUNet ID should be able to access it, though you may need to email your faculty mentor to request an account.  Jobs are submitted using the [slurm workload manager](https://slurm.schedmd.com/documentation.html), and you can access the system using `ssh` with your SUNet credentials at `[SUNetID]@login.sherlock.stanford.edu`. When you log in, you'll have access to a home directory (you can get the path via the bash variable `$HOME`) and a scratch directory where you should put large output files (the relevant path will be accessible through the bash variable `$SCRATCH`.) For KIPAC, the partition line in your slurm job files can be something like `#SBATCH --partition=kipac,iric,hns`.

Useful links:
* Some other wiki information is [here](https://github.com/KIPAC/computing/tree/master/sherlock)
* [Official Sherlock page] (http://sherlock.stanford.edu/mediawiki/index.php/Main_Page), including [introductory documentation](https://www.sherlock.stanford.edu/docs/overview/introduction/)
* [Status page](https://status.sherlock.stanford.edu/)


