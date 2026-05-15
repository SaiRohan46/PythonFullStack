#Hello day 3

'''
Program to convertb 24hrs  clock into normal
'''
time="20:37"
parts=time.split(":")
hours=parts[0] 
print(type(hours))
#cant make additions as string operations
hours=int(parts[0])
mins=int(parts[1])
print(f"{time} is converted into : {hours-12}:{mins} pm")

#LISTS
'''
--->List is a collection of different datatypes and represented in square
     brackets and seperated by ,
--->List is mutable
    '''
any = [1,"python",[1,2,[34,"this is python 3rd class",78],
                   "Python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])
'''
LIST METHODS
--------------------------------------
1) APPEND
--->this method is used to add new items into the list at last index position
Syntax : var_name.append(item)
--->cant add two items
'''
any=[1,2,3]
any.append(6)
print(any)
any.append([20,90])
print(any)

'''
#STRINGS ARE IMMUTABLE EXAMPLE
--------
Immutable ---> could nt be able to modify that variable
example = int,str
--------
Mutable ---->Can be abled to modify that variable
example =  lst
'''
so="Python is a "
print(so.replace("P","s"))
print(so)
any=[1,2,3]

print(any.append(6))
print(any)
'''
---------------------------------------
2) EXTEND
--->this also adds to the last but add itterable into list,
    each value of the substring in each index of the list
Syntax : var_name.extend(itterable)
'''
any = [1,2,3]
print(any.extend([4]))
print(any)
'''
----------------------------------------
3) POP
---> Used to remove a iteam from the list,by mentioning the index position
Syntax : var_name.pop(index)
'''
any = [1,2,3]
print(any.pop(0)) # returns what is popped
print(any)
'''
-----------------------------------------
4) REMOVE
---> Used to remove a specific item from the list
Syntax : var_name.remove(item)
'''
any=[1,2,3]
any.remove(2)
print(any)
