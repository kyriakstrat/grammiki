import numpy as np
from fractions import Fraction

'''
# max z = 2x1 + 4x2+x3+x4
# st
#      x1 + 3x2 + x4<=  8
#     2x1 + x2 <= 6
#      x2+4x3+x4 <=  6
# x1, x2,x3,x4 >= 0
'''

#basic vars x1,x2,x3
B = np.array([[1,3,0],
              [2,1,0],
              [0,1,4]])

N = np.concatenate((np.array([1,0,1]).reshape(3,-1),np.eye(3)),axis=1)



B_inv = np.linalg.inv(B)
x = np.array([2,3,1]).reshape(1,3).dot(B_inv.dot(N))
print(x)
x = np.array([1,0,0]).reshape(1,3).dot(B_inv.dot(N))
print(x)
