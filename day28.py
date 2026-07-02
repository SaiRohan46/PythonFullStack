#Hello day-28
'''
Matplotlib
----------
--> This is a library in python for data visualization, allowing users to
    create a variety of plots....

Basic structure of Matplotlib
-----------------------------
--> Figure
--> Axes
--> Grid
--> Title
--> Legend


import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.bar(sales,values)
plt.xlabel
plt.show()

import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.bar(sales,values,color='green',edgecolor='black')
plt.xlabel('Car Models')
plt.ylabel('Values')
plt.title('BMW Car Sales')
plt.show()

import matplotlib.pyplot as  plt
overs=[1,2,3,4,5]
scores=[4,19,36,20,8]
plt.plot(overs,scores,color='green')
plt.title('Score card')
plt.xlabel('Overs')
plt.ylabel('Score')
plt.show()

import matplotlib.pyplot as plt
subjects=['Python','Java','DA']
students=[24,6,11]
plt.pie(students,labels=subjects,autopct='%1.1f%%')
plt.legend()
plt.title('Students in Courses')
plt.show()

import matplotlib.pyplot as plt
y=[10,15,18,20,25]
plt.hist(y,bins=4)
plt.grid()
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
'''


























































