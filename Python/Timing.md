# Using timing and profilers

I've put some example code in the [xipe](xipe) sub-directory.

In particular, the [xipe/code_to_profile.py](xipe/code_to_profile.py) script.
Again, to avoid having to change code during the demo, I put in some options to
turn on and off the profiling


Ok, let's start by using the unix `time` command to see how long this piece of code takes.

```console
(kipac) ada$ time python xipe/code_to_profile.py 
python xipe/code_to_profile.py  3.67s user 0.05s system 27% cpu 13.739 total
```

That is slower than expect, but maybe it taking time to load some libraries of a disk or something like that.
Let's time just code itself, using some code like this side the script.

```python
    import time

    t0 = time.time()
    main()
    t1 = time.time()

    print("Code ran in %0.2f s" % (t1 - t0))
```


```console
(kipac) ada$ python xipe/code_to_profile.py -t
Code ran in 13.63 s
```

Ok, that is slower that expected, and it looks like the code is taking most of the time.  Let's profile it, using
some code like this.


```python
    import cProfile
    import pstats
    from pstats import SortKey

    cProfile.run('main()', 'prof.stats')
    p = pstats.Stats('prof.stats')
    p.strip_dirs().sort_stats(SortKey.CUMULATIVE)
    p.print_stats(30)
```
	

```console
(kipac) ada$ python xipe/code_to_profile.py -p
Mon Apr  5 20:05:38 2021    prof.stats

         4000089 function calls (4000084 primitive calls) in 14.388 seconds

   Ordered by: cumulative time
   List reduced from 52 to 30 due to restriction <30>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   14.388   14.388 {built-in method builtins.exec}
        1    0.001    0.001   14.387   14.387 <string>:1(<module>)
        1    0.001    0.001   14.387   14.387 code_to_profile.py:39(main)
        1    0.000    0.000   14.366   14.366 code_to_profile.py:29(integrate_v1)
        1    0.000    0.000   10.002   10.002 code_to_profile.py:26(func_that_does_nothing_except_sleep)
        1   10.002   10.002   10.002   10.002 {built-in method time.sleep}
        1    0.540    0.540    4.351    4.351 code_to_profile.py:19(func_with_unneeded_bound_check)
  1000002    2.467    0.000    2.467    0.000 code_to_profile.py:7(sinxcosx)
  1000001    0.452    0.000    1.355    0.000 code_to_profile.py:14(check_bounds)
  1000001    0.214    0.000    0.902    0.000 code_to_profile.py:10(format_error_message)
  1000001    0.689    0.000    0.689    0.000 {method 'format' of 'str' objects}
      8/3    0.001    0.000    0.022    0.007 {built-in method numpy.core._multiarray_umath.implement_array_function}
        2    0.000    0.000    0.018    0.009 <__array_function__ internals>:2(trapz)
        2    0.010    0.005    0.017    0.008 function_base.py:3980(trapz)
        1    0.000    0.000    0.016    0.016 code_to_profile.py:34(integrate_v2)
        2    0.000    0.000    0.006    0.003 <__array_function__ internals>:2(diff)
        2    0.006    0.003    0.006    0.003 function_base.py:1141(diff)
        1    0.000    0.000    0.004    0.004 <__array_function__ internals>:2(linspace)
        1    0.001    0.001    0.004    0.004 function_base.py:26(linspace)
        1    0.003    0.003    0.003    0.003 {built-in method numpy.arange}
        3    0.001    0.000    0.001    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        2    0.000    0.000    0.001    0.000 {method 'sum' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.001    0.000 _methods.py:36(_sum)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(any)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2236(any)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:73(_wrapreduction)
        1    0.000    0.000    0.000    0.000 {method 'any' of 'numpy.generic' objects}
        1    0.000    0.000    0.000    0.000 _methods.py:44(_any)
        8    0.000    0.000    0.000    0.000 _asarray.py:88(asanyarray)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.normalize_axis_index}
```

Ok, right away two things stand out.
	1. Spending 10 seconds in func_that_does_nothing_except_sleep() seems like a waste of time.
	2. There are 1000001 calls to check_bounds, format_error_message, str.format() and sinxcosx(), probably we can avoid some of those.


```
(kipac) ada$ python -i xipe/code_to_profile.py -p 
...

>>> p.print_callers(30)
   Ordered by: cumulative time
   List reduced from 52 to 30 due to restriction <30>

Function                                                                 was called by...
                                                                             ncalls  tottime  cumtime
{built-in method builtins.exec}                                          <- 
<string>:1(<module>)                                                     <-       1    0.000   14.270  {built-in method builtins.exec}
code_to_profile.py:39(main)                                              <-       1    0.001   14.269  <string>:1(<module>)
code_to_profile.py:29(integrate_v1)                                      <-       1    0.000   14.248  code_to_profile.py:39(main)
code_to_profile.py:26(func_that_does_nothing_except_sleep)               <-       1    0.000   10.005  code_to_profile.py:29(integrate_v1)
{built-in method time.sleep}                                             <-       1   10.005   10.005  code_to_profile.py:26(func_that_does_nothing_except_sleep)
code_to_profile.py:19(func_with_unneeded_bound_check)                    <-       1    0.528    4.230  code_to_profile.py:29(integrate_v1)
code_to_profile.py:7(sinxcosx)                                           <- 1000001    2.374    2.374  code_to_profile.py:19(func_with_unneeded_bound_check)
                                                                                  1    0.011    0.011  code_to_profile.py:34(integrate_v2)
code_to_profile.py:14(check_bounds)                                      <- 1000001    0.439    1.328  code_to_profile.py:19(func_with_unneeded_bound_check)
code_to_profile.py:10(format_error_message)                              <- 1000001    0.203    0.889  code_to_profile.py:14(check_bounds)
{method 'format' of 'str' objects}                                       <- 1000001    0.685    0.685  code_to_profile.py:10(format_error_message)
{built-in method numpy.core._multiarray_umath.implement_array_function}  <-       1    0.000    0.000  <__array_function__ internals>:2(any)
                                                                                  2    0.000    0.006  <__array_function__ internals>:2(diff)
                                                                                  1    0.000    0.004  <__array_function__ internals>:2(linspace)
                                                                                  1    0.000    0.000  <__array_function__ internals>:2(ndim)
                                                                                  1    0.000    0.000  <__array_function__ internals>:2(result_type)
                                                                                  2    0.001    0.018  <__array_function__ internals>:2(trapz)
<__array_function__ internals>:2(trapz)                                  <-       1    0.000    0.013  code_to_profile.py:29(integrate_v1)
                                                                                  1    0.000    0.005  code_to_profile.py:34(integrate_v2)
function_base.py:3980(trapz)                                             <-       2    0.010    0.017  {built-in method numpy.core._multiarray_umath.implement_array_function}
code_to_profile.py:34(integrate_v2)                                      <-       1    0.000    0.017  code_to_profile.py:39(main)
<__array_function__ internals>:2(diff)                                   <-       2    0.000    0.006  function_base.py:3980(trapz)
function_base.py:1141(diff)                                              <-       2    0.006    0.006  {built-in method numpy.core._multiarray_umath.implement_array_function}
<__array_function__ internals>:2(linspace)                               <-       1    0.000    0.004  code_to_profile.py:39(main)
function_base.py:26(linspace)                                            <-       1    0.001    0.004  {built-in method numpy.core._multiarray_umath.implement_array_function}
{built-in method numpy.arange}                                           <-       1    0.003    0.003  function_base.py:26(linspace)
{method 'reduce' of 'numpy.ufunc' objects}                               <-       2    0.001    0.001  _methods.py:36(_sum)
                                                                                  1    0.000    0.000  _methods.py:44(_any)
{method 'sum' of 'numpy.ndarray' objects}                                <-       2    0.000    0.001  function_base.py:3980(trapz)
_methods.py:36(_sum)                                                     <-       2    0.000    0.001  {method 'sum' of 'numpy.ndarray' objects}
<__array_function__ internals>:2(any)                                    <-       1    0.000    0.000  function_base.py:26(linspace)
fromnumeric.py:2236(any)                                                 <-       1    0.000    0.000  {built-in method numpy.core._multiarray_umath.implement_array_function}
fromnumeric.py:73(_wrapreduction)                                        <-       1    0.000    0.000  fromnumeric.py:2236(any)
{method 'any' of 'numpy.generic' objects}                                <-       1    0.000    0.000  fromnumeric.py:73(_wrapreduction)
_methods.py:44(_any)                                                     <-       1    0.000    0.000  {method 'any' of 'numpy.generic' objects}
{built-in method numpy.core._multiarray_umath.normalize_axis_index}      <-       2    0.000    0.000  function_base.py:1141(diff)
_asarray.py:88(asanyarray)                                               <-       2    0.000    0.000  function_base.py:26(linspace)
```                                                                                  2    0.000    0.000  function_base.py:1141(diff)
                                                                                  4    0.000    0.000  function_base.py:3980(trapz)

