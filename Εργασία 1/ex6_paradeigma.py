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
#maxZ = 3x1+2x2
#periorismoi
#x1+x2+x3 = 9
#3x1+x2+x4 = 18
#x1+x5 = 7
#x2+x6 = 6

C = np.array([3,2,0,0,0,0]) #sintelestes antikeim synart
A = np.array([[1,1],
             [3,1],
             [1,0],
             [0,1]])
b = np.array([9,18,7,6])
A = np.concatenate((A,np.eye(4),b.reshape(4,-1)),axis=1) #pinakas sintelestwn 
 

z = np.zeros(7).reshape(1,-1)

 #basic vars
basis = [2,3,4,5]
it = 1
while(True):
    profit = z[0][-1]
    print("iteration:",it)
    printer(A,basis,profit)
    C_z = C-z[:,:len(A[0])-1]
    #the var that will be selected
    col = list(C_z[0]).index(max(C_z[0]))           

    #row = list(b/A[:,col]).index(0,min(b/A[:,col])) 
    
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

    z = np.dot(C[basis].reshape(1,-1),A)
    it+=1
    if(np.all(C_z<=0)): #sinthiki termatismou
        print("done")
        break
    x = input("continue?")
    if(x=='n'):break
