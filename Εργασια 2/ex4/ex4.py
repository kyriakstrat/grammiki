import numpy as np 

A = np.array([[1,1,0,-1,0,2,-2],
              [0,1,0,-1,1,-2,2],
              [0,1,1, 0,0,1,-1],
              [0,1,0,-1,0,-1,1]])
b = np.array([6,4,2,1]).reshape(-1,1)
c = np.array([1,2,1,-3,1,1,-1]).reshape(-1,1)
x0 = np.array([7,0,2.5,0,3,0,0.5]).reshape(-1,1)

y0 = np.dot(A,x0)

print(np.dot(c.T,x0))
print(np.dot(b.T,y0))