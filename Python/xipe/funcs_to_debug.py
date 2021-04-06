#!/usr/bin/env python

import argparse
import pdb

def makeMeAList():
    return [1, 2, 3, 7, 11, 13, 17]


def makeMeADict():
    return {1:1, 2:2, 3:3, 4:7, 5:11, 6:13, 7:17}

A_LIST = makeMeAList()
A_DICT = makeMeADict()


class AClasssyClass:

    def __init__(self):

        self._a_list = A_LIST
        self._a_dict = A_DICT

    def this_function_works(self, item):

        idx = self._a_list.index(item)
        if idx < 0:
            print("Item %s is not on list" % item)
            return 
        print("Item %s is element %i on list" % (item, idx))


    def this_function_usually_works(self, key):

        val = self._a_dict.get(key, None)
        if val is None:
            print("Key %s is not in dict" % key)
            return 
        print("Key %s points to value %s in dict" % (key, val))

        
    def this_function_has_a_bug(self, item, debug=False):

        if debug:
            pdb.set_trace()
            
        found_it = None
        for idx, test_val in enumerate(self._a_list):
            if test_val == item:
                found_it = test_val
        if found_it is None:
            found_idx = None
            print("Item %s is not on list" % item)
            return
        found_idx = idx        
        print("Item %s is element %i on list" % (item, idx))

                

# argument parser
parser = argparse.ArgumentParser(prog='funcs_to_debug.py')
parser.add_argument('-b', '--bugs', help='Bugs == True?', action='store_true', default=False)
parser.add_argument('-d', '--debug', help='Run in debug mode', action='store_true', default=False)        
parser.add_argument('-g', '--global_debug', help='Run in global debug mode', action='store_true', default=False)        

# unpack options
args = parser.parse_args()

# pdb can also be a useful tool to learn about how a piece of code works
if args.global_debug:
    pdb.set_trace()

classMcClassface = AClasssyClass()

if args.bugs:
    print()
    print("List = ", A_LIST)
    for an_item in A_LIST:    
        classMcClassface.this_function_has_a_bug(an_item, args.debug)
else:
    print()
    print("List = ", A_LIST)
    for an_item in A_LIST:
        classMcClassface.this_function_works(an_item)
    print()
    print("Dict = ", A_DICT)
    for a_key in A_DICT:
        classMcClassface.this_function_usually_works(a_key)











