import numpy as np

# SHAPE
np.shape


# RESHAPE AN ARRAY
test_score
array([ 0.66666667,  0.76086957,  0.80072464,  0.80434783,  0.8115942 ,
        0.8115942 ,  0.80797101,  0.8115942 ,  0.80797101,  0.8115942 ])

# reshape it to 5 arrays & 2 in each array
test_score.reshape(5,2)
array([[ 0.66666667,  0.76086957],
       [ 0.80072464,  0.80434783],
       [ 0.8115942 ,  0.8115942 ],
       [ 0.80797101,  0.8115942 ],
       [ 0.80797101,  0.8115942 ]])



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
nparray.max()       #max
np.argmax(result)   #get index with max result; need to flatten if its multi-dimensional


# HISTOGRAM
np.histogram(array, bins=10, range=(0,1000)) #give two arrays binned, first is x-values, 2nd y-values or range
#(array([139,  17,  13,   9,   7]),
#array([    0.,   200.,   400.,   600.,   800.,  1000.]))