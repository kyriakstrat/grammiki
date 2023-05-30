import numpy as np
from scipy import linalg
# −3x1 + 2x2 + 8x3 ≤ 17
# −x1 + x2 + 3x3 ≤ 9
# −2x1 + x2 + 8x3 ≤ 16
# x1, x2, x3 ≥ 0

A = np.array([[-3,2,8],
              [-1,1,3],
              [-2,1,8]])
I = np.eye(3)
A = np.concatenate((A,-I))
B = np.array([17,9,16,0,0,0])


# A = np.array([[1,1,1],[2,2,1],[1,-1,0],[-1,0,0],[0,0,-1]]) 
# B = np.array([3,4,0,0,0])

it = 0 
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            it+=1
            print(it)
            print('A:')
            print(A[[i,j,k]])
            print('B:')
            print(B[[i,j,k]])
            try:
                x = linalg.solve(A[[i,j,k]],B[[i,j,k]])
                y = np.dot(A,x)
                if np.all(y<=B):
                    print('valid')
                else:
                    print('invalid')
                print('x:')
                print(x)
                
            except:
                print("adinato sistima")
            print("\n")