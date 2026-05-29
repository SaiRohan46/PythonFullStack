#Hello day 15
'''
MODULES
-------------------
--> A module in python is a file that contain a python code  such as
--> variables
--> functions
--> classes
--> statements
TWO TYPES OF MODULES
----------------------
1) USER DEFINED
2) BUILT IN

import Modules
print(Modules.add(1,2))


import math
print(math.sqrt(5))
print(math.sqrt(144))

from math import sqrt
print(sqrt(25))

import os
os.mkdir("Some_Python")
os.rmdir("Some_Python")

import sys
print(sys.version)
print(sys.exit)
print(sys.path)

import random
print(random.randint(1000,9999))

from collections import Counter
data = ['a','b','c','d']
counter=Counter(data)
print(counter)

from collections import Counter,defaultdict
data = ['a','b','c','d']
counter=Counter(data)
print(counter)
dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)

TASK
------
1) == IS
2) EXTEND APPEND
3) MUTABLE IMMUTABLE
4) MEMORY ALLOCATION IN PYTHON
5) GENERATORS
'''
