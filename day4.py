#Hello day4
a=90
b=8
print(a+b)
# CONCATENATION
'''
--> "+" FOR INTEGERS ADD THEM ,FOR OTHER DATATYPES LIKE LIST ,STR,TUPLE THEY
     GET CONCATENATED
'''
any="p"
so="is"
print(any+so)
an=[1,2]
na=[2,3]
print(an +na)
'''
---------------
3) TUPLES
---> COLLECTION OF DIFFERENT DATATYPES SEPERATED BY COMMAS , REPRESENTED IN
       "(  )" AND IMMUTABLE
       ---> METHODS IN TUPLE :
       1) count()
          --> to count a particular iteam in the tuple
          Syntax : var_name.count(item)
       2) index()
          --> used to find out the index position of the item,only gives the
              first occurance
          Syntax : var.name_index(value)
---------------
'''
some=(1,"Python",[1,2],((3,4),(5,6)),"Python")
print(some.index("Python"))
print(some.count("Python"))
print(some[1][1])
print(some[3][1][1])
'''
----------------
4) DICTIONARY
----> DICT IS A KEY : VALUE PAIRS,KEY AND VALUES ARE SEPERATED BY :,
      KEY VALUE PAIRS ARE SEPERATED BY ,
----> REPRESENTED BY {} CURLY BRACES
----> ONLY IMMUTABLE DATATYPES ARE USED A KEYS Eg : int,str,tuples
       list are mutable so cant be used as keys
----> VALUES CAN BE ANY DATATYPES

    ---> METHODS IN DICT :
    1) keys() :
       ----> returns all the keys
       Syntax  : dict.keys()
    2) values() :
       ----> returns values
       Syntax : dict.values()
    3) items() :
       ----> used to get key and value pairs together
       Syntax : dict.items()
    4) update() :
       ----> used to add a new key:value pair into dict
       Syntax : dict.update({key : value})
    5) OTHER WAY TO UPDATE :
       Syntax : dict['key']="new_value"
'''
details = {"Name" : "Rohan" , 1:2,(1,2):[3,4]}
print(details)
print(type(details))

print(details)
print(type(details))
det = {"Name" : " Rohan",
       "age" : 45 ,
       "MobN" : 1234567}
print(det.keys())
print(det.values())
print(det.items())

print(det["age"])
det.update({"AAdharN" : 1234567890})
print(det)
det['Name'] = "Rohannn"
print(det)
































