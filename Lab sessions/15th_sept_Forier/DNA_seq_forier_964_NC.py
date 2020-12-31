#Author: Jai Kumar Roll No.: 15076

from matplotlib.pylab import *
from math import *
import cmath
import numpy as np
'''FORIER TRANSFORM: Xk=sum(0,N-1) xn*e**(2*pi*i*k*n/k)
			will get periodicity at k=3(k gives periodicty)
'''

def forier(S):
	Ns=len(S)
	Xk=[]
	x=[]
	for k in range(Ns):
		u=0.0
		v=0.0
		for i in range(0,Ns):
			u+=S[i]*np.sin(2.0*pi*k*i/Ns)
			v+=S[i]*np.cos(2.0*pi*k*i/Ns)
		Xk.append(sqrt(u**2+v**2))
		x.append(k)
	return [Xk,x]
#reading dna sequence
f=open('DNA_Seq/NC_000964.fna','r')
A=[]
for i in f:
    l=i.split()
    A+=l
B=[]
for i in range(len(A)):
    B+=A[i]
f.close()
f=open("NC_000964.ptt",'r')
NC=[]
for i in f:
	i1=i.split()
	NC.append([i1[0],i1[1]])
f.close()
x=[]
y=[]
for i in range(10):
	X=B[int(NC[i][0]):int(NC[i][1])]
	S1=[1 if i=='A' else 0 for i in X]
	S2=[1 if i=='T' else 0 for i in X]
	S3=[1 if i=='C' else 0 for i in X]
	S4=[1 if i=='G' else 0 for i in X]	
	Xk1=forier(S1)
	Xk2=forier(S2)
	Xk3=forier(S3)
	Xk4=forier(S4)
	Xk=[]
	for j in range(len(Xk1[0])):
		Xk.append(Xk1[0][j]**2+Xk2[0][j]**2+Xk3[0][j]**2+Xk4[0][j]**2)
	Ns=len(X)
	print Ns
	Xk=Xk[1:]
	n=Xk[int(math.floor(Ns/3))]*1.0/np.mean(Xk)
	#plot(Xk1[1][1:],Xk[1:])
	#show()
	print n
	y.append(n)
	x.append(i)
scatter(x,y)
show()
