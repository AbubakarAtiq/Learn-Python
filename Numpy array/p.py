"""
    Numpy Arrays#
#Getting started
Numpy arrays are great alternatives to python lists. Some of the key advantages
 of numpy arrays are that they are fast, easy to work with, and give users the opportunity
 to perform calculations across entire arrays.
 In the following example, you will first create two python lists. Then, you
 will import the numpy package and create numpy arrays out of the newly created
 lists.
 """
height=[1.11, 1.22, 1.33,1.44,1.55,1.66]
weight=[2.11,2.22,2.33,2.44,2.55,2.66]
#import the numpy package as np
import numpy as np
#Create 2 numpy arrays from height and weight
np_height= np.array(height)
np_weight= np.array(weight)
print(type(np_height)) 
print(np_height,np_weight)