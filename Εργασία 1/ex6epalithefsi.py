import numpy as np
from scipy import linalg

#antikimeniki sinartisi
#maxZ = x1+4x2+5x3
#periorismoi
#x1+2x2+3x3+x4=2
#3x1+x2+2x3+x5 = 2
#2x1+3x2+x3+x6 = 4


A = np.array([[1,2,3],[3,1,2],[2,3,1]])
I = np.eye(len(A))
A = np.concatenate((A,I),axis=1)
b = np.array([2,2,4])


# C = A[:,[3,4,5,6]]
# B = np.dot(linalg.inv(C),b)
# print(B)

maxx = -100
it = 0 
for i in range(len(A[0])):
    for j in range(i+1,len(A[0])):
        for k in range(j+1,len(A[0])):
            it+=1
            print(it,":")
            try:
                xyz = np.zeros(7)
                B = np.dot(linalg.inv(A[:,[i,j,k]]),b)
                print(i,j,k)
                xyz[[i,j,k]] = B 
                print(xyz)
                print('value:',1*xyz[0]+4*xyz[1]+5*xyz[2])
                for num in B:
                    if num < 0 :
                        print("invalid")
                        break
                else:
                    print("valid!")
                    if(1*xyz[0]+4*xyz[1]+5*xyz[2]>maxx):
                        maxx=1*xyz[0]+4*xyz[1]+5*xyz[2] 
                        x = xyz[0]
                        y = xyz[1]
                        z = xyz[2]
            except:
                print("matrix is singular")
            print("\n")
print(maxx)
print(x,y,z)