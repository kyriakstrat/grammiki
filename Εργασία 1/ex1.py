from turtle import color
import matplotlib.pyplot as plt
import numpy as np

def solver(z,xpoints,ypoints):
    maxx = -1000
    for i in range(len(xpoints)):
        if z(xpoints[i],ypoints[i])>maxx:
            maxx = z(xpoints[i],ypoints[i])
            point = xpoints[i],ypoints[i]
    plt.scatter([point[0]],[point[1]],color='yellow')
    return(maxx,point)



#antikeimenikes synartiseis
def z1(x,y):
    return 2*x-5*y

def z2(x,y):
    return 2*x-4*y

def z3(x,y):
    return 2*x-3*y

plt.plot([0,0],[0,5],label='x1=0')
plt.plot([0,5],[0,0],label='x2=0')


plt.plot([0,2],[4,0],label='2x1+x2=4') #2x1+x2=4
plt.plot([0,5],[2.5,0],label='x1+2x2=5') #x1+2x2-5=0
plt.plot([1,5],[0,2],label='x1-2x2=1') #x1-2x2-1=0
#lyseis
plt.plot([0.5,5],[0,1.8],label='2x1-5y=1(Z1)') #2x1-5y=1
plt.plot([1.5,5],[0,2.33],label='2x1-3y=3(Z3)') #2x1-5y=1
xpoints =[0,1,3]
ypoints = [4,2,1]
plt.scatter(xpoints,ypoints,color='red')
# plt.scatter([3],[1],color="red")
leg = plt.legend(loc='upper right')
plt.xlabel("x1")
plt.ylabel("x2")
print(solver(z1,xpoints,ypoints))   
plt.show()


