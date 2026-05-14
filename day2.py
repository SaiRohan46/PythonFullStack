#Hello day 2 --- 14/05/2026
'''

Operators
1.Arithematic
---------------
+,-,*,/,%,//,**
print(2*3)
print(4%5 == 0)
print(10**2)
print(10/2)
print(35.20//5)

2.Assignment
----------------
=,+=,-=,*=,%= ---> operator
count=0
for j in range(1,10):
    count+=1
print(count)

3.Comparison
-----------------
== ---> LOOK BOTH VALUES ARE EQUAL OR NOT
!= , >= , <= , > , <
a=[1,2]
b=[1,2]
print(a == b)

4.Logical
-----------------
and -> USED TO CHECK WHETHER BOTH ARE TRUE
or
not

a=[1,2]
b =[1,2]
c=a
print(type(a))
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is not b)

a=5
if a%3==0 or a%5==0:
    print("true")


5.Membership
-----------------
in
not in

a=7
b=[1,2]
print(a in b)
print(a not in b)

6.Identity
-----------------
is ---> THIS OPERATOR LOOKS FOR THE OBJECT IS SAME OR NOT,
isnot

7.Bitwise
-----------------
&,|,<<,>>
5 ---> 0101
3 ---> 0011

print(5&3)
print(5|3)
'''

#------------------------------------
#STRINGS
'''
String is a sequence of characters that are enclosed in '',"",''''''

any = " python "
'''
#METHODS
'''
--------------
replace() ---> Used to replace with a new sub string
syntax : variable_name.replace("old string","new string")

any = " python is a language "
print(any.replace("python","Java"))
print(any)
---------------
#split()---> used to seperate in parts and split based on substring where
              before substring is one index and after is another
              index iin the list
syntax : variable_name.spiit("substring")

any = " python is a language "
print(any.split("$"))
print(any.split("is"))
print(any.split("a"))
----------------
len() ---> get number of items in a substring

any = "Python is a Lanhguage"
print(any.len())
-----------------
slicing() ----> can give the access to get the particular part from one to
               other index in the string
syntax ---> variable_name[starting index : ending index ]

c
print(any[3:11])
------------------
indexing ----> print the character that is present in a index of a string
               only one value at a time

any = "Python is a Language"
print(any[7])
print(any.index("ang")) #returns the index where a starts -- 13
-------------------
join() ----> add a value after every substring
syntax : variablename.join(".")
-------------------

            

      
