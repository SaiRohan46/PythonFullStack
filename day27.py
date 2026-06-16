#Hello Day-27
'''
                    DATA ANALYSIS
                   ---------------
--> This is the process of inspecting,cleaning,transforming,and modeling data
    to discover useful insights...
    
Types of Data Analysis
----------------------

1.Descriptive Analysis
----------------------
--> Summarizing data

2.Diagnostic Analysis
----------------------
--> Understanding Causes

3.Predictive Analysis
-----------------------
--> Forecasting Future Outcomes

4.Prescriptive Analysis
-----------------------
--> Suggesting Actions based on data

Why DA ?
--------
--> To improve Decision Making
--> Detects Trends & Patterns


    ---------------
    **** NumPy ****
    ---------------
--> NumPy Fullform Numerical Python
--> This python library is for numerical computations,it provides support for
    multi-dimensional arrays,and Linear Algebra Operations,making it essential
    data analytics...
    
Using Numpy in DA
-----------------
--> Improved Performance
--> Simplifies Complex Operations
--> Easy Data Manipulation


import numpy as np
arr1=np.array([[1,4,7,9],[5,6,7,8],[1,2,3,4]])
print(arr1)
print(arr1.shape)
reshaped=arr1.reshape(6,2)
print(reshaped)


import numpy as np
arr2=np.array([1,2,30,33,50,6,70])
print(arr2[3])
print(arr2 + 5)

import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(np.dot(arr1,arr2))

-- SHALLOW COPY AND DEEP COPY --
import numpy as np
arr1=np.array([10,20,30])

nrm_copy=arr1.view()
arr1[0] = 100
print(nrm_copy)
print(arr1)

copy_dee=arr1.copy()
arr1[1] = 200
print(copy_dee)
print(arr1)


    ----------------
    **** Pandas ****
    ----------------
--> The pandas is a powerful data manipulation and analysis library..
--> Where it provides data structure like series and dataframes for efficiency
    in data handling...


import pandas as pd
an = pd.Series([2999,15999,52999,4999,1999],
               index=['Earbuds','Smartphone','Lap','Watch','Footwear'])
print(an)

METHODS FOR Series()
--------------------
1.mean()
2.sum()
3.max()
4.min()
5.apply()
6.map()

DataFrame
----------
'''
import pandas as pd 
data = {
    'Product':['Earbuds','Smartphone','Lap','Watch','Footware'],
    'Brand':['Noise','OnePlus','HP','Bolt','Nike'],
    'Price':[1599,15999,53999,1999,3999],
    'Stock':[50,15,25,40,70]
    }
dip=pd.DataFrame(data)
print(dip)
dip=pd.DataFrame(data,index=range(1,6))
print(dip)


























