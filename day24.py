#Hello day24
'''
                     Regular Expressions (RegEX)
                     ----------------------------
--> It is a sequence of characters that form a searching pattern...
--> This can be used to check if a strig containthe specified search pattern
--> Python has a built in -package called 're' which can be usedw to work with
    RegEx

import re
x=input()
if re.fullmatch(r'[0-9]{10}',x):
    print("valid number")
else:
    print("Invalid Number")
Meta Characters:
----------------
[] --> a-z,A-Z,0-9 and any specified sequence
.  --> Each dot is a char
^  --> This look for the string that start with sequence or not
$  --> This look for the string is ending with the sequence or not
*  --> Zero or more occurances
+  --> One or more Occurances
?  --> Zero or one
{} --> Specify Range

Special Sequence
----------------
\S --> No space
\s --> Only space
\D --> Non-Digits
\d --> Only-Digits
\w --> Matches any letters digits underscores
\W --> Spaces and Special Symbols

a="C is a foundational programming Language found in 1972"

import re
print(re.findall('[a-mA-Z]',a))
print(re.findall('[a]',a))
print(re.search('[als]',a))
print(re.findall('fo.....',a))
print(re.search('fo.....',a))
print(re.findall('^C is',a))
print(re.search('^C is',a))
print(re.search('1972$',a))
print(re.findall('1972$',a))
print(re.findall('pr.?g',a))
print(re.findall('pr.?og',a))
print(re.findall('p.{7}',a))
'''
import re
x=input()
if re.fullmatch(r'^[+]91[6-9][0-9]{9}$',x):
    print("Valid number")
else:
    print("Invalid Number")


