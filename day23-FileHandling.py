#Hello day-23
'''
              FILE HANDLING
              --------------
--> File Handler is an objecr of file to maintain several function of file
    like creating,reading,updating and delrting the file..
 OPEN A FILE
 ------------
 1.open()
 2.with open()

 Syntax: so = open('filename','mode')
         -----
         -----
         name.close()


 MODES
 -----
 1.'r'--> Its used in reading the file,error if file doesn't exist
 2.'a'--> Its used to add the text into file at last index,
          If the file doesnt exist it will creat one with a name
 3.'w'--> Its used to add the text but it will overwrite the complete file
          If the file doesnt exist it will creat one with a name
 4.'x'--> Used to create the file but throws error if we use 'r' mode to create

so = open('demo.txt','r')
print(so.read())
so.close()

so = open('demo.txt','a')
print(so.write('Rohan'))
so.close()


so = open('dem.txt','w')
print(so.write('Rohan'))

with open('demo.txt','w') as so:

METHODS
-------
1.write()
2.read()
  -> This method can read entire file chunk by chunk where we can specify the
      size

3.readline()
  -> It can read only one line at a time in a file
4.readlines()
  -> It will read entire file and gives in a list where each line is each
     index in the list

with open('rohan.txt','r') as rr:
    print(rr.readlines())
    
with open('rohan.txt','r') as rr:
    print(rr.readline())

'''
import os
os.remove("rohan.txt")
os.remove("demo.txt")

