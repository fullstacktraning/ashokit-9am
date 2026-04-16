import numpy as np

list1 = np.array([10,20,30,40,50])
print(list1)
print(list1.shape) #(5,)
print(list1.ndim)  #1
print(list1.dtype) #int64

list2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(list2.shape) #(3, 3)
print(list2.ndim)  #2
print(list2.dtype) #int64