# Tips for improving your python experience

Python is really good at some things.

However, python is also very bad at a lot of the thing that you want to do all the time.  That is probably the single
most useful thing to understand about python.

In short,
  1. python is great for scripting and terrible for computations.
  2. python is great for get started with simple projects and lousy
     for maintaing large, complicated projects.  This is doubly true
     of jupyter notebooks.

For 1) the point is that python is not the thing you want use to do your computations, but
rather the thing that you use to interact with some piece of code that
will actually do your computations.

For 2) the point is that people have developed tools to make it easier
to use python in complicated projects.

This tutorial, originally presented as a Dark Energy Science
Collaboration (DESC) seminar, collects 4 tips that have helped me
vastly improve my python experience.


## Installation 

You can use conda to easily install the packages you will need to run these examples

    conda create -n kipac -y -c conda-forge python=3.8 numpy pylint flake8 black jupyter
    git clone https://github.com/KIPAC/BootCamp
    cd BootCamp/Python


## Unlocking the power of numpy

From the numpy website: https://numpy.org/

    The core of NumPy is well-optimized C code. Enjoy the flexibility of Python with the speed of compiled code.

    Fast and versatile, the NumPy vectorization, indexing, and
    broadcasting concepts are the de-facto standards of array
    computing today.

	NumPy’s high level syntax makes it accessible and productive for programmers from any background or experience level.

The first two points are certainly true.  The third point is
debatable, but the intention is certainly there.

So, to use numpy well, it help to understand the "vectorization,
indexing, and broadcasting concepts".

This notebook will work through those concepts:

[Numpy concepts](./Numpy.ipynb)


This notebook, the third in a series of notesbooks about python, also
has many useful numpy tips:

[Numpy and scipy section of python tutorial](./Python \(3\).ipynb)



## Code linters

This notebook demonstrates some of the limitations of python and
notebooks when it comes to developing a large project:

[Python Limitations](./StuffNotToDoInNotebooks.ipynb)

Code checking or 'linting' tools are one of the best ways to address
those limitations.

There are a number of python 'linters'.

This unix-based demo will show how to use a couple of linters:

[Linting](./Linting.md)




## Using pdb: the python debugger and python -i

One of the main reasons that peoople tend to continue developing a project
in jupyter notebooks long past the point where they should probably
switch over to making a python package and modules is that notebooks
provide a flexible and interactive debugging enviroment.

This unix-based demo will show how to use the interactive prompt and pdb:

[Debugging](./Debugging.md)


## Profilers and timers

Profiling / timing code is always useful, as it help identify
ineffciencices.  It is doubly important when using python.

Because python is very slow compared to the underlying code
that libraries such as "numpy" and "scipy" use, it is possible to have
a piece of code take many times longer b/c of the specific
implementation.

Using Profiling / timing lets you see how the actual execution
time matches against your expectations of how long the code will take.

This unix-based demo will show how to use timers and profilers:

[Timing](./Timing.md)



## Other tutorials

This tutorial lives in the https://github.com/KIPAC/BootCamp
repository.  The other tutorials in this repository were
orignally developed in support of a several session "BootCamp" for
new members of the Kavli Institute for Particle Astrophyscis and
Cosmology (KIPAC) at Stanford and SLAC National Lab.   Many of these
tutorials were updated in 2020 to help incoming summer students get
started with their interships while working remotely.

Some of the tutorials are very general, others are quite specific to
SLAC/ Stanford / KIPAC computing resources.



