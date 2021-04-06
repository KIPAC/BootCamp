#!/usr/bin/env python

import argparse
import time
import numpy as np

def sinxcosx(val):
    return np.sin(val) * np.cos(val)

def format_error_message(**kwargs):
    error_message_format = "Bounds error {i} not in range[{min_val}, {max_val}]"
    return error_message_format.format(**kwargs)

def check_bounds(i, a_vect):
    formatted_message = format_error_message(i=i, min_val=0, max_val=a_vect.size+1)
    if i < 0 or i >= a_vect.size:
        raise ValueError(formatted_message)            

def func_with_unneeded_bound_check(a_vect):
    out_array = np.zeros((a_vect.shape))
    for i, val in enumerate(a_vect):
        check_bounds(i, a_vect)
        out_array[i] = sinxcosx(val)
    return out_array
        
def func_that_does_nothing_except_sleep():
    time.sleep(10)

def integrate_v1(xvals):
    yvals = func_with_unneeded_bound_check(xvals)
    func_that_does_nothing_except_sleep()
    return np.trapz(xvals, yvals)
    
def integrate_v2(xvals):
    yvals = sinxcosx(xvals)
    return np.trapz(xvals, yvals)
    

def main(fast=False):
    XVALS = np.linspace(0., np.pi/4, 1000001)
    if not fast:
        v1 = integrate_v1(XVALS)
    v2 = integrate_v2(XVALS)



               

# argument parser
parser = argparse.ArgumentParser(prog='code_to_profile.py')
parser.add_argument('-p', '--profile', help='Profile code', action='store_true', default=False)
parser.add_argument('-t', '--time', help='Time code', action='store_true', default=False)        
parser.add_argument('-f', '--fast', help='Fast version', action='store_true', default=False)        

# unpack options
args = parser.parse_args()
    

if args.profile:
    
    import cProfile
    import pstats
    from pstats import SortKey

    if args.fast:
        cProfile.run('main(True)', 'prof.stats')
    else:
        cProfile.run('main()', 'prof.stats')
    p = pstats.Stats('prof.stats')
    p.strip_dirs().sort_stats(SortKey.CUMULATIVE)
    p.print_stats(30)


elif args.time:

    t0 = time.time()
    main(args.fast)
    t1 = time.time()

    print("Code ran in %0.2f s" % (t1 - t0))
    

else:

    main(args.fast)
