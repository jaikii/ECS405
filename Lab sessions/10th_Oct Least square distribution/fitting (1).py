from matplotlib.pylab import *
import random
y=[]
x=[]
m1=2
c11=3
y1=[m1*i+c11 for i in range(100)]
mx=[];my=[]
for j in range(10,1000,2):
	for i in range(100):
		y.append(y1[i]+(j*random.random()- j/2))
		x.append(i)
	z=[]
	c1=0;c2=0;c3=0;c4=0
	#fitting
	for i in range(len(x)):
		c1+=x[i]
		c2+=x[i]**2
		c3+=y[i]
		c4+=x[i]*y[i]
	n=len(x)
	m=(c1*c3-(n)*c4)/(c1**2-(n)*c2)
	c=(c1*c4-c2*c3)/(c1**2-(n)*c2)
	print m,c
	#for i in range(len(x)):
	#	z.append(m*x[i]+c)

	#scatter(x,y)
	#plot(x,y1,color='red')
	#plot(x,z,color='black')
	my.append(abs(m-m1)*100/m)
	mx.append(j)
plot(mx,my)
show()
