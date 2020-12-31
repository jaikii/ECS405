from matplotlib.pylab import *
from math import *
import glob
path = 'DNA/*.fna'   
files=glob.glob(path)
for file in files: #will read all the files from DNA folder
	f=open(file,'r')
	x=[]
	for i in f:
	    l=i.split()
	    x+=l
	y=[]
	for i in range(len(x)):
	    y+=x[i]
	f.close()
	N=len(y)

##function to find the distribution
	def cot(y,x):
		z={}
		s=1
		for i in range(len(y)):
			z[i]=0
		for i in range(len(y)):
			if y[i]!=x:
				s=s+1
			else:
				z[s]=z[s]+1
				s=1
		for i in range(len(z)):
			if z[i]==0:
				del z[i]
		for i in z.keys():	#probability
			z[i]=log(z[i]*1.0/N)
		return z

##Function to fit the points
	def fit(x,y):
		c1=0;c2=0;c3=0;c4=0
		for i in range(len(x)):
			c1+=x[i]
			c2+=x[i]**2
			c3+=y[i]
			c4+=x[i]*y[i]
		n=len(x)
		m=(c1*c3-(n)*c4)/(c1**2-(n)*c2)
		c=(c1*c4-c2*c3)/(c1**2-(n)*c2)
		return [m,c]
	A=cot(y,'A')
	cut=50				#cutting at 50
	A1=fit(A.keys()[:cut],A.values()[:cut])
	xA=[i for i in A.keys()]
	xA=xA[:cut]
	yA=[A1[0]*xA[i]+A1[1] for i in range(len(xA))] 

##ERROR
	error1=0
	error2=0
	sumy=0
	for i in range(len(xA)):
		error2+=(yA[i]-A[xA[i]])**2
		sumy+=abs(A[xA[i]])
		error1+=abs(yA[i]-A[xA[i]])
	print "error1(%)= ",error1*100/sumy
	s=sqrt(error2)/sumy
	print "error2(%)= ",s*100
	scatter(A.keys(),A.values(),color='red',label="w.r.t 'A'")
	plot(xA,yA,color='black')
	legend()
	savefig("%s_4_fitting.pdf"%file)
	show()
