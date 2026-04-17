import numpy as np

# Example-1
# list1 = np.array([10,20,30,40,50])
# print(list1)
# print(list1.shape) #(5,)
# print(list1.ndim)  #1
# print(list1.dtype) #int64

# list2 = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])
# print(list2.shape) #(3, 3)
# print(list2.ndim)  #2
# print(list2.dtype) #int64

# Example-2
# print( np.zeros((2,3)) )
# print( np.ones((2,3)) )
# print( np.eye(3) )
# print( np.arange(0,10,2) )
# print( np.linspace(0,1,5) )

# Example-3
# list1 = np.array([10,20,30,40,50])
# print(list1[0]) #10
# print(list1[-5]) #10
# print(list1[1:3]) #1 will include and 3 will execlude [20,30] 
# print(list1[1:])  #1 to end [20,30,40,50]
# print(list1[:3])  # 0 will include and 3 will exclude [10,20,30]

# Example-4
# list1 = np.array([[1,2,3],
#                   [4,5,6]])
# print( list1[0][0] ) #1
# print(list1[1][2] )  #6
# print(list1[:,0]) # col1
# print(list1[:,1]) # col2
# print(list1[:,2]) # col3

# print(list1[0]) # row1
# print(list1[1]) # row2

# Example-5
# list1 = np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])
# print(list1[:,0])
# print(list1[:,0:2])
# print(list1[0:2])

# Example-6
# Vectorization
# list1 = np.array([1,2,3])
# print(list1 + 2)
# print(list1 - 2)
# print(list1 * 2)
# print(list1 / 2)
# print(list1 ** 2)

# Example-7
# list1 = np.array([1,2,3,4,5])
# print(f'min element {np.min(list1)}')
# print(f'max element {np.max(list1)}')
# print(f'sum of element {np.sum(list1)}')
# print(f'mean of elements {np.mean(list1)}')
# print(f'square of element {np.sqrt(list1)}')

# Example-8
# list1 = np.array([1,2,3])
# list2 = np.array([[10],[11],[12]])
# print(list1 + list2)

# Example-9
# list1 = np.array([[1,2],
#                   [3,4]])
# list2 = np.array([[5,6],
#                   [7,8]])
# print(np.dot(list1,list2))




