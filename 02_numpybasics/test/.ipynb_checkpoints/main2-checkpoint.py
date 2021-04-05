import numpy
narray4 = numpy.arange(1,10)
narray5 = numpy.arange(11,20)
narray6 = numpy.array([narray4,narray5])

narray7 = numpy.array([narray6,narray6])

#print(narray6[0][4])
#print(narray6[0, 4])
print(narray7[1, 0, 4])
print(narray7[1][0][4])