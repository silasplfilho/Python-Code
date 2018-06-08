from numpy import *

a = arange(15).reshape(3, 5)
a
a.shape
a.ndim
a.dtype.name
a.itemsize
a.size
type(a)
b = array([6, 7, 8])
type(b)
#-------------------
# ARRAY CREATION
a = array([2, 3, 4])
a

b = array( [ (1.5, 2, 3), (4,5,6) ] )
b
c = array( [ (1.5, 2, 3), (3,4) ] )
