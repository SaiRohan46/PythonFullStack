#Hello day-5
'''
  SETS
----------------
--> A SET IS A COLLECTION OF UNIQUE AND UNORDERED ELEMENTS
--> DUPLICATE VALUES ARE NOT ALLOWED
--> REPRESENTED IN CURLY BRACES {}
--> ITEMS ARE NOT STORED IN INDEX ORDER

 METHODS
 -------------
 1) UNION :
    --> it will give two sets elements into a  single set
    Syntax : var_name.union(another_var)
    
 2) INTERSECTION :
    -->  it will give the elements that are common in both sets
    Syntax : var_name.intersection(another_var)
    
 3) DIFFERENCE :
    --> to get the elements that are not common in respective set
    Syntax : var_name.difference(another_var)

 4) SYMMETRIC DIFFERENCE :
    --> to get the elements which are not common in both sets removes the
        common elements and returns remaining all in one set
    Syntax : var_name.symmetric_difference(another_var)

 5) ADD :
    --> to add new elements into set
    Syntax : var_name.add(element).add()
 6) UPDATE :
    --> adds multiple elements
    Syntax : var_name.update([elements])
    

 7) sum(set_name),max(set_name),min(set_name) -->same as list

 8) REMOVE :
    --> Used to remove an element from the set but throws error(key error)
        if element is not there
    Syntax : var_name.remove(value)
    
 9) DISCARD :
    --> used to remove element but never throws error if element not there
    Syntax : var_name.discard(value)
'''
any={1,2,3,3,4}
print(any)
an = {64,54}
print(any | an)
print(any.union(an))


a={1,2,3,4}
b={5,6,7}
print(a & b)
print(a.intersection(b))

r={1,2,3,4,5,6}
s={3,4,5,9}
print(r - s)
print(r.difference(s))


print(r ^ s)
print(r.symmetric_difference(s))
print(a.symmetric_difference(b))

z={1,2,3,4,5}
z.add(56)
print(z)


x={1,2,3,4,5}
x.remove(5) #if element doesnt exists throws error
print(x)
# 5 already removed
x.discard(5)
print(x) #doesnt throw error if element not there


x={1,2,3,4,5}

print(sum(x))

























