# Coding practice and software development

### Some comments

Coding itself is not for the purpose of writing code. Coding should serve a specific purpose.
Writing clean and result orientated code, which is re-usable and able to evolve within a collaborative
environment is a key component to successful and efficient projects, not just in business but also
in the scientific environment.


### Goals

Exposure and pointers to tools and approaches that are beyond specific lines of code.

### Version control

Version control allows to:
- have (full) control over the history of the work (ou crap, I just messed up my code -> just go back to the version where it used ). There is no need for version_1, _final, _veryfinal_veryveryfinal…
- collaborate on a project, merge code in a clean and controllable way
- distribute code over multiple machines and users, and keeping the local code up to date

Advice: 
- make small incremental commits
- give MEANINGFUL commit statements
- use different branches for developments

Version control is meant for code/text/LateX, but not for data!

What is git version control, see e.g. [this link](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

### Integrated development environment (IDE)

What is an IDE: see e.g. [wikipedia](https://en.wikipedia.org/wiki/Integrated_development_environment)
An IDE helps keeping the structure in your code, recognises simple typos and errors in your structure, allows integration with version control and many more useful tools.

Recommended for Python: [PyCharm Community edition (free)](https://www.jetbrains.com/pycharm/download/)



### Interactive python interface: ipython/jupyter notebook

You want to interact with your code, produce plots, try out other configurations, show what you’ve done to your collaborators -> The jupyter notebook is exactly what you want! Just type:
```
>>> jupyter notebook
```
For a documentation, see e.g. [this link](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.ipynb#)

Note: The notebook is NOT meant to write your code in! It is meant to allow for an interacting execution of your code/software. You can easily import your code with packaging (see below).



### Packaging your code

You want to import your code and make it usable as “normal” software, such as numpy, scipy etc? 
That’s simply done by adding certain files and structure to your code -> and its software!

Automatised packaging can be done with [cookiecutter](https://github.com/audreyr/cookiecutter-pypackage) (very easy, don’t worry).
```
>>> cookiecutter https://github.com/Nekroze/cookiecutter-pypackage.git
```
And then follow the terminal (provide your name, package name etc…)

This packaging enables to install and add the path to the software is recognised on your machine. This makes it easy to reuse your software for other purposes, import it with the entitled name and make it being used by your collaborators or the entire community.

How to install your code:
```
>>> cd code_repository (where the setup.py file is stored)
>>> python setup.py install --user
```

And the code is installed (the path to the software is recognised on your machine). You can now import your code in any other software you are executing on your machine.
 
If you are changing the code/developing it, you should install the software in development mode (it will recognise changes and keeps the path up to date with your development)
```
>>> python setup.py develop --user 
```
If you don’t know the difference between sudo and --user, see e.g. [this ressource](http://askubuntu.com/questions/641182/upgrade-python-packages-with-pip-use-sudo-or-user)
 


### Testing your code

You want to be sure that your code is doing that it supposed to do? 
You want to make sure if you change something in your code that it still performs as it is supposed to? 
You don’t want to spend hours in looking at random positions in your code to find the bug? 
That is what integrated testing is for.

Getting used to writing testing code and running this code in parallel is now considered a good habit. 
Used wisely, this method helps you define more precisely your code’s intent and have a more decoupled architecture. 
More about how to write tests for Python can be found [here](http://docs.python-guide.org/en/latest/writing/tests/)

The packaging of your code (cookiecutter) allows for integrated testing.



### Document your code

Document every single definition in your code with specifics about the data format and what the definition is doing before writing the actual code. 
This helps also structure your code better. A documentation guideline for Python can be found [here](https://www.python.org/dev/peps/pep-0008/)

Packaging with cookiecutter can enable automated generation of documentations (as you may know them from numpy, scipy etc).


### Profiling your code

Is the wall time execution of your code a limiting factor to produce results? 
Often you can easily improve the performance of your code by a factor of a few when you know where the bottlenecks are. 
Profiling allows to identify those bottlenecks and can compare different implementations of your code.

Profiling can be done within a jupyter notebook. See [this link](http://pynash.org/2013/03/06/timing-and-profiling/) for a detailed description.

