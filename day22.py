#Hello day 22
'''
try:
    print(10/0)
except:
    print("This will handle Zero Error ! ")

try:
    print("a")
except:
    print("This will handle Name Error")
else:
    print("No error")

try:
    print(5+"Py")
except NameError:
    print("This will handle Name Error")
else:
    print("No Error")

-->Only First Error Gets executed no other  error would get entering the
    except block 
try:
    print(a)
    print(5+7)
except:
    print("This is a Name error")
else:
    print("No error")

---->First error "is" handled by the "except" block
try:
    print(a)
    print(5+"Py")
except TypeError:
    print('This will handle TypeError')
except NameError:
    print('This handles NameError')
else:
    print('No Error')

FINALLY IN PYTHON
-----------------
--> This will be executed either try block contain error or not...
'''
try:
    print("Haiii")
except TypeError:
    print("This will handle TypeError")
except NameError:
    print("This will handle NameError")
finally:
    print("This End")
