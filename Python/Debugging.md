# Using interactive mode and pdb to debug


I've put some example code in the [xipe](xipe) sub-directory.

In particular, the [xipe/funcs_to_debug.py](xipe/funcs_to_debug.py) script has a bug in it.

First, let's run it without the bug.

```console
(kipac) ada$ python xipe/funcs_to_debug.py 

List =  [1, 2, 3, 7, 11, 13, 17]
Item 1 is element 0 on list
Item 2 is element 1 on list
Item 3 is element 2 on list
Item 7 is element 3 on list
Item 11 is element 4 on list
Item 13 is element 5 on list
Item 17 is element 6 on list

Dict =  {1: 1, 2: 2, 3: 3, 4: 7, 5: 11, 6: 13, 7: 17}
Key 1 points to value 1 in dict
Key 2 points to value 2 in dict
Key 3 points to value 3 in dict
Key 4 points to value 7 in dict
Key 5 points to value 11 in dict
Key 6 points to value 13 in dict
Key 7 points to value 17 in dict
(kipac) ada$ 
```


Now let's turn on the bug.

```console
(kipac) ada$ python xipe/funcs_to_debug.py --bugs

List =  [1, 2, 3, 7, 11, 13, 17]
Item 1 is element 6 on list
Item 2 is element 6 on list
Item 3 is element 6 on list
Item 7 is element 6 on list
Item 11 is element 6 on list
Item 13 is element 6 on list
Item 17 is element 6 on list
```


Ok, lets use python in interactive mode to investigate.

```console
(kipac) ada$ python -i xipe/funcs_to_debug.py --bugs        

List =  [1, 2, 3, 7, 11, 13, 17]
Item 1 is element 6 on list
Item 2 is element 6 on list
Item 3 is element 6 on list
Item 7 is element 6 on list
Item 11 is element 6 on list
Item 13 is element 6 on list
Item 17 is element 6 on list
>>> 
>>> 
>>> classMcClassface
<__main__.AClasssyClass object at 0x7fcd4850b310>
>>> classMcClassface._a_list
[1, 2, 3, 7, 11, 13, 17]
>>> dir(classMcClassface)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_a_dict', '_a_list', 'this_function_has_a_bug', 'this_function_usually_works', 'this_function_works']
>>> classMcClassface.this_function_has_a_bug()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: this_function_has_a_bug() missing 1 required positional argument: 'item'
>>> classMcClassface.this_function_has_a_bug(7)
Item 7 is element 6 on list
```

Ok, seems like we've found the function with the bug, let's use pdb to have a closer look.
The requires two lines of python

```python
import pdb
pdb.set_trace()
```

Here is a nice cheat sheet for pdb:
[pdf cheat sheet](https://kapeli.com/cheat_sheets/Python_Debugger.docset/Contents/Resources/Documents/index)

I've actually already added them to the example so I don't have to edit the file while doing the demo.

```console
(kipac) ada$ python -i xipe/funcs_to_debug.py --bugs --debug

List =  [1, 2, 3, 7, 11, 13, 17]
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(47)this_function_has_a_bug()
-> found_it = None
(Pdb) list
 42         def this_function_has_a_bug(self, item, debug=False):
 43     
 44             if debug:
 45                 pdb.set_trace()
 46     
 47  ->         found_it = None
 48             for idx, test_val in enumerate(self._a_list):
 49                 if test_val == item:
 50                     found_it = test_val
 51             if found_it is None:
 52                 found_idx = None
(Pdb) where
  /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(79)<module>()
-> classMcClassface.this_function_has_a_bug(an_item, args.debug)
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(47)this_function_has_a_bug()
-> found_it = None
 (Pdb) next
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(48)this_function_has_a_bug()
-> for idx, test_val in enumerate(self._a_list):
(Pdb) next
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(49)this_function_has_a_bug()
-> if test_val == item:
(Pdb) test_val
1
...
(Pdb) next
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(51)this_function_has_a_bug()
-> if found_it is None:
(Pdb) next
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(55)this_function_has_a_bug()
-> found_idx = idx
(Pdb) idx
6
(Pdb) idx = 0
(Pdb) next
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(56)this_function_has_a_bug()
-> print("Item %s is element %i on list" % (item, idx))
(Pdb) next
Item 1 is element 0 on list
(Pdb) continue
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(47)this_function_has_a_bug()
-> found_it = None
```



I've also found pdb is useful for code exploration:


```console

(kipac) ada$ python xipe/funcs_to_debug.py -g            
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(73)<module>()
-> classMcClassface = AClasssyClass()
(Pdb) list
 68     
 69     # pdb can also be a useful tool to learn about how a piece of code works
 70     if args.global_debug:
 71         pdb.set_trace()
 72     
 73  -> classMcClassface = AClasssyClass()
 74     
 75     if args.bugs:
 76         print()
 77         print("List = ", A_LIST)
 78         for an_item in A_LIST:
(Pdb) step
--Call--
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(19)__init__()
-> def __init__(self):
(Pdb) step
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(21)__init__()
-> self._a_list = A_LIST
(Pdb) step
> /Users/echarles/software/KIPAC/BootCamp/Python/xipe/funcs_to_debug.py(22)__init__()
-> self._a_dict = A_DICT
(Pdb) continue

List =  [1, 2, 3, 7, 11, 13, 17]
Item 1 is element 0 on list
Item 2 is element 1 on list
Item 3 is element 2 on list
Item 7 is element 3 on list
Item 11 is element 4 on list
Item 13 is element 5 on list
Item 17 is element 6 on list

Dict =  {1: 1, 2: 2, 3: 3, 4: 7, 5: 11, 6: 13, 7: 17}
Key 1 points to value 1 in dict
Key 2 points to value 2 in dict
Key 3 points to value 3 in dict
Key 4 points to value 7 in dict
Key 5 points to value 11 in dict
Key 6 points to value 13 in dict
Key 7 points to value 17 in dict
```

