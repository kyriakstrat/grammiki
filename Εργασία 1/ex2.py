from turtle import color
import matplotlib.pyplot as plt

def solver(xpoints,ypoints):
    minn = 1000
    #antikeimeniki sinartisi 
    def z(x,y):
        return 6*x+7.5*y
    #ypologismos veltistis korifis
    for i in range(len(xpoints)):
        if z(xpoints[i],ypoints[i])<minn:
            minn = z(xpoints[i],ypoints[i])
            point = xpoints[i],ypoints[i]
    plt.scatter([point[0]],[point[1]],color='yellow')
    return(minn,point)


#periorismoi 
plt.plot([0,0],[0,1],label="x1=0")
plt.plot([0,1],[0,0],label="x2=0")
plt.plot([0,1],[1,0],label="x1+x2=1")
plt.plot([0.9,0.15],[0,1],label="12x1+9x2=10.8") #12x1+9x2=10.8
plt.plot([0.85,0.1],[0,1],label='6x1+4.5x2=5.1') #6x1+4.5x2=5.1
plt.plot([1,0],[0.266,0.93],label='6x1+9x2 = 8.4') #6x1+9x2 = 8.4
#lysi
plt.plot([1,0],[0.08,0.88],label="6x1+7.5x2=6.6(Z)") #12x1+9x2=10.8
#efikta simia tomis periorismwn 
xpoints =[0.4,0.6]
ypoints = [0.6,0.4]

#labels kai setup gia to diagramma
leg = plt.legend(loc='upper right')
plt.xlabel("x1")
plt.ylabel("x2")
#plot simeiwn korifwn
plt.scatter(xpoints,ypoints,color='red')

print(solver(xpoints,ypoints))   
plt.show()
