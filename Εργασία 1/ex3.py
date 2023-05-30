import numpy as np
from scipy import linalg


def printer(A,basis,profit):
    print("tablaue:")
    print(A[:,:len(A[0])-1])
    print("basic vars")
    print(basis)
    print(A[:,-1])
    print("profit:")
    print(profit)


#antikimeniki sinartisi
#minZ=-x1-4x2-5x3 => maxZ = -170x1-160x2-175x3-180x4-2925
#periorismoi
#x1+x5 = 48
#x1+x2+x6 = 79
#x1+x2+x3+x7 = 87
#x2+x3+x8 = 64
#x3+x4+x9 = 82
#x4+x10 = 52

 #sintelestes antikeim synart
C = np.array([170,160,175,180,0,0,0,0,0,0])
b = np.array([48,79,87,64,82,52])

#tablaue sintelestwn 
A = np.array([[1,0,0,0],
              [1,1,0,0],
              [1,1,1,0],
              [0,1,1,0],
              [0,0,1,1],
              [0,0,0,1]
             ])
A = np.concatenate((A,np.eye(len(A)),b.reshape(len(b),-1)),axis=1)
 

z = np.zeros(len(A[0])).reshape(1,-1)

#basic vars
basis = [4,5,6,7,8,9]
it = 1
while(True):
    profit = z[0][-1]
    print("iteration:",it)
    printer(A,basis,profit)
    C_z = C-z[:,:len(A[0])-1]
    #the var that will be selected
    col = list(C_z[0]).index(max(C_z[0]))           

    #find the var that will be taken out
    minn = 1000
    for i in range(len(A)):
        if(A[i][col]>0 and A[i][-1]/A[i][col]<minn):
            minn = A[i][-1]/A[i][col]
            row = i

    #allagi twn vasikwn metavlitwn
    basis[row] = col                                
    pivot = A[row,col]

    #grammoprajeis
    A[row,:] = A[row,:]/pivot

    for i in range(len(A)):
        div = A[i,col]
        if(i==row):continue
        A[i,:] = A[i,:]-div*A[row,:]

    #evresi kerdwn 
    z = np.dot(C[basis].reshape(1,-1),A)

    #epanalipsi
    it+=1
    print(C_z)
    #sinthiki termatismou
    if(np.all(C_z<=0)): 
        print("done")
        break

