import numpy as np

# SHAPE
np.shape

# CREATE ARRAY
list = [1,2,3,4]
np.array(list)


# space out between a start & end number of equal intervals
np.linspace(2.0, 3.0, num=5)
np.linspace(2,3,5)  #It is ok not to define num=
#>>> array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])


# FLATTEN
a = np.array([[1,2], [3,4]])
a.flatten()
#>>> array([1, 2, 3, 4])

# ZEROS
np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])

np.zeros((5,5))
array([[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]])

# SORT
nparry = [1,2,3,4,5,6]
np.sort(nparray) #ascending order
np.sort(nparray)[::-1] #descending order
np.sort(nparray)[::-1][:5] #top 5 descending


# CALCULATIONS

np.mean(nparray)    #mean