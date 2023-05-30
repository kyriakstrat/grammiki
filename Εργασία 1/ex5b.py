import numpy as np
from scipy import linalg
# −3x1 + 2x2 + 8x3 ≤ 17
# −x1 + x2 + 3x3 ≤ 9
# −2x1 + x2 + 8x3 ≤ 16
# x1, x2, x3 ≥ 0
#minZ = 12x1 -10x2-30x3

A = np.array([[-3,2,8],
              [-1,1,3],
              [-2,1,8]])
I = np.eye(len(A))
A = np.concatenate((A,I),axis=1)
b = np.array([17,9,16])
C = [[12,-10,-30,0,0,0]]

# C = A[:,[3,4,5,6]]
# B = np.dot(linalg.inv(C),b)
# print(B)

minn = 1000
it = 0 
for i in range(len(A[0])):
    for j in range(i+1,len(A[0])):
        for k in range(j+1,len(A[0])):
            it+=1
            print("iteration",it,": basis:",i,j,k)
            try:
                xyz = np.zeros(6)
                B = np.dot(linalg.inv(A[:,[i,j,k]]),b)
                xyz[[i,j,k]] = B 
                xyz = xyz.reshape(-1,1)
                val = np.dot(C,xyz)
                print('[x1,x2,x3]=',xyz[[0,1,2]].reshape(1,-1)[0])
                print('value=',val[0][0])
                for num in B:
                    if num < 0 :
                        print("invalid")
                        break
                else:
                    print("valid!")
                    if(val<minn):
                        minn = val[0][0]
                        x = xyz[0][0]
                        y = xyz[1][0]
                        z = xyz[2][0]
            except:
                print("matrix is singular")

print("minimum solution:")
print("(x1,x2,x3) = (",x,y,z,')')
print('Z=',minn)
