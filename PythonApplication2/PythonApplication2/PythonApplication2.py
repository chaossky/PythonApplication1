import numpy as np
a=np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(type(a))

b=np.ndarray([6,7,8])
print(b)
print(type(b))
