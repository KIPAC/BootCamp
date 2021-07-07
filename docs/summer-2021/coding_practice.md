# Coding practice and software development

### Prelude

Coding itself is not for the purpose of writing code. Coding should serve a specific purpose.
Writing clean and result orientated code, that is re-usable and able to evolve within a collaborative
environment is a key component to successful and efficient projects, not just in business but also
in the scientific environment.


### Goals

The aim of this page/lecture is to introduce and point at a set of tools commonly used in the software development community.
We also highlight the purpose and usefulness of certain tools. The notes are not meant to be complete and a lot of documentation and examples can be found in the web.

### Version control

Version control allows to:
- have (full) control over the history of the work (ou crap, I just messed up my code -> just go back to the version where it used to work). There is no need for version_1, _final, _veryfinal_veryveryfinal…
- collaborate on a project, merge code in a clean and controllable way
- distribute code over multiple machines and users, and keeping the local code up to date
- branch-out: explore and experiment with features and design patterns, even if they might at the end not be part of the 'main' branch

Advice: 
- make small incremental commits
- give MEANINGFUL commit messages
- use different branches for specific developments

Version control is meant for code/text/LateX, but not for data!

What is git version control, see e.g. [this link](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).


### Integrated development environment (IDE)

What is an IDE: see e.g. [wikipedia](https://en.wikipedia.org/wiki/Integrated_development_environment)
An IDE assists in:
- keeping the structure in your code
- recognizing simple typos and errors in your structure
- allows integration with version control 
- ...and many more useful tools.

Recommended for Python: [PyCharm Community edition (free)](https://www.jetbrains.com/pycharm/download/)



### Interactive python interface: ipython/jupyter notebook

You want to interact with your code, produce plots, try out other configurations, show what you’ve done to your collaborators -> The jupyter notebook is exactly what you want! Just type:
```
>>> jupyter notebook
```
For a documentation, see e.g. [this link](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.ipynb#)

Note: The notebook is NOT meant to write your code in! It is meant to allow for an interacting execution of your code/software. 
You can easily import your code with packaging (see below).

To share your notebooks, there are cloud solutions that set up an environment and allow you to execute the notebooks on the cloud.
Check out [goolge colab](https://colab.research.google.com/notebooks/intro.ipynb).

Note: If you want your software (right software not code!) be executable on the cloud, you need to package it and make it publicly available! (see next section)



### Packaging your code

You want to import your code and make it usable as “normal” software, such as numpy, scipy etc? 
That’s simply done by adding certain files and structure to your code -> and its software!

Automatised packaging can be done with e.g., [cookiecutter](https://github.com/audreyr/cookiecutter-pypackage) (very easy, don’t worry).
```
>>> cookiecutter https://github.com/Nekroze/cookiecutter-pypackage.git
```
And then follow the terminal (provide your name, package name etc…)

This packaging enables you to install and the path to the software is recognised on your machine. 
This makes it easy to reuse your software for other purposes, import it with the entitled name and make it being used by
your collaborators or the entire community. (or make notebooks being executed in the cloud, see colab above)

How to install your code:
```
>>> cd code_repository (where the setup.py file is stored)
>>> python setup.py install --user
```

And the code is installed (the path to the software is recognised on your machine).
You can now import your code in any other software you are executing on your machine.
 
If you are changing the code/developing it, you should install the software in development mode
(it will recognise changes and keeps the path up to date with your development)
```
>>> python setup.py develop --user 
```
If you don’t know the difference between sudo and --user, see e.g. [this ressource](http://askubuntu.com/questions/641182/upgrade-python-packages-with-pip-use-sudo-or-user)
 


### Testing your code

You want to be sure that your code is doing that it supposed to do? 
You want to make sure if you change something in your code that it still performs as it is supposed to? 
You don’t want to spend hours in looking at random positions in your code to find the bug? 
That is what integrated testing is for.

Getting used to writing tests and running the test code in parallel to the development of the actual software is now considered the standard, not just a good habit. 
Used wisely, writing the test functions before or during the actual development helps you to define more precisely your code’s intent and purpose and to have a more decoupled architecture. 
More about how to write tests for Python can be found e.g. [here](http://docs.python-guide.org/en/latest/writing/tests/)

The packaging of your code (e.g., cookiecutter) conveniently allows for integrated testing.



### Document your code

Document every single definition in your code with the specifics about the data format and what the definition is doing before writing the actual code. 
This helps also structure your code better. A documentation guideline for Python can be found [here](https://www.python.org/dev/peps/pep-0008/)

Packaging with cookiecutter and working with an IDE can enable automated generation of documentation boxes to be filled in  (as you may know them from numpy, scipy etc).


### Profiling your code

Is the wall time execution of your code a limiting factor to produce results? 
Often you can improve the performance of your code by a factor of a few when you know where the bottlenecks are. 
Profiling allows you to identify those bottlenecks and you can also compare different implementations of your code.

Profiling can be done within a jupyter notebook. See [this link](http://pynash.org/2013/03/06/timing-and-profiling/) for a detailed description.

