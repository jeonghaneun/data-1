import numpy

narray1 = numpy.array([1,2,3,3])
narray2 = numpy.array([1,2,3,3])
narray3 = numpy.array([narray1,narray2])
narray4 = numpy.array([range(10)])
narray5 = numpy.arange(11,20)
narray7 = numpy.array([narray5,narray5])
narray8 = numpy.array([narray7,narray7])
print(narray8)
print(narray8.ndim)
print(narray8[1,0,4])


#git init
#git add___filename_or_.___
#git commit -m "__________" -upgrade memo
#git remote add origin(name) _______(http://)
#git push -u(upstream) origin(name) 