#This program only works in Py 2
import numpy as np

c = np.loadtxt("C:/Users/mlgpr/Google Drive/Coding/data.txt",dtype="string",delimiter=",")
shape = c.shape
dims = c.ndim

print c
print "Dimension Count: {}".format(dims)
print "Shape: {}".format(shape)
