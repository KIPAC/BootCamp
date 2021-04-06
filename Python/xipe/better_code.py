#!/usr/bin/env python
""" Implements a class that prints 'Hello World' """

class BetterClass:
    """ A class that prints a string """

    def __init__(self, toPrint="Hello World"):
        """ Constructor, takes the string to print """
        self._data_member = toPrint

    def print_it(self):
        """ Prints the data member """
        print(self._data_member)

    @property
    def data(self):
        """ Returns the data member """
        return self._data_member

BETTER = BetterClass()
BETTER.print_it()
