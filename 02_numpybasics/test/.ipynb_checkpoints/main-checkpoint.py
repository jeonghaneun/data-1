import numpy

narray1 = numpy.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0])
narray2 = numpy.array([range(10)])
narray3 = numpy.arange(10)

narray4 = numpy.arange(1,10)
narray5 = numpy.arange(11,20)
narray6 = numpy.array([narray4,narray5])

narray7 = numpy.array([narray6,narray6])
#print(narray7.shape)
print(type(narray1))
#ndarray=n-dimensional array 
#print(narray1.dtype)
#print(narray1.ndim)
