#!/usr/bin/env python
import argparse
import os
from glob import *


class WorstClassEver(object):
    def __init__(self):
        try:
            print("I'm going to print a variable that does not exist", self.missing)
            import copy
        except Exception as msg:
            pass
        try:
            print(
                "Now I'm gonna call a functin that does not exist", self.missingFunc()
            )
        except:
            pass
        if False:
            return "constructors shouldn't return things"
        elif True:
            print("No need to have elif after a return statement")
        else:
            print("This statement is pointless")

    def functionWithTooManyArgs(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        return None

    def functionWithUndefinedVars(self):
        return arg1 * arg2

    def functionThatDefinesDataMembers(self):
        self._data_member = None

    def functionWithBrutalistWhitespace(self):
        s = (
            "Some people really care about whitespace"
            + " and linters can help"
            + " "
            + "with that"
        )
        t = (1, 3, 32, 41, 3)
        v = 1 + 5
        print(s)

    def functionThatDoesDumbThingsWithLists(self):
        l = list([a for a in (1, 2, 4)])
        for x in l:
            try:
                l.pop(x)
            except:
                return False
        return None

    def functionThatMessesUpScope(self, unused=None):
        l = [1, 3, 4]
        for x in l:

            def double_it(x):
                return 2

            x = double_it(x)

        def halve_it(x):
            return x / 2.0

        x = halve_it(x)

    def functionThatDoesDumbThingsWithDicts(self):
        d = dict({a: a for a in (1, 2, 4)})
        for k, v in d.items():
            d.pop(x)

    def functionWithShadowIterator(self, arg1, arg2):
        arg3 = None  # unused
        for arg2 in arg1:  # shadows arg2
            if arg2 is arg1:
                print(f"%arg1 is %arg1")


class ChildOfWorstClass(WorstClassEver):
    def __init__(self, some_arg={}):
        super(ChildOfWorstClass, self).__init__()

    def functionThatDoesDumbThingsWithDicts(self, var=1e4):
        super(ChildOfWorstClass, self).functionThatMessesUpScope(self)


worst = ChildOfWorstClass()
worst.functionWithBrutalistWhitespace()
worst.functionThatDoesDumbThingsWithLists()
worst.functionThatDoesDumbThingsWithDicts()
worst.functionWithShadowIterator([3, 4], None)
try:
    just_bad = worst / 2.0
except:
    pass
