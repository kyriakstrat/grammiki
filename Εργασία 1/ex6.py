import numpy as np
from scipy import linalg


def printer(A,basis,profit):
    print("tablaue:")
    print(A)
    print("basic vars")
    print(basis)
    print(A[:,-1])
    print("profit:")
    print(profit)


#antikimeniki sinartisi
#minZ=-x1-4x2-5x3 => maxZ = x1+4x2+5x3
#periorismoi
#x1+2x2+3x3+x4=2
#3x1+x2+2x3+x5 = 2
#2x1+3x2+x3+x6 = 4

 #sintelestes antikeim synart
C = np.array([1,4,5,0,0,0])
b = np.array([2,2,4])

#tablaue sintelestwn 
A = np.array([[1,2,3],
              [3,1,2],
              [2,3,1],
             ])
#[Α|Ι|b]
A = np.concatenate((A,np.eye(len(A)),b.reshape(len(b),-1)),axis=1)
 

z = np.zeros(len(A[0])).reshape(1,-1)

#basic vars
basis = [3,4,5]
it = 1
while(True):
    profit = z[0][-1]
    print("iteration:",it)
    printer(A,basis,profit)
    
    C_z = C-z[:,:len(A[0])-1]
    print("C-z:")
    print(C_z)
    #the var that will be selected
    col = list(C_z[0]).index(max(C_z[0]))           

    #find the var that will be taken out
    minn = 100
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
    #sinthiki termatismou
    if(np.all(C_z<=0)): 
        print("done")
        break
