from matplotlib.pylab import *
from math import *
F=open("sequence.fasta",'r')
F.readline()
x=[]
for line in F:
	lines=line.split()
	x=x+lines
y=str()
for i in range(len(x)):
	y=y+x[i]
x=[]
# giving the values to DNA seq. as G=1 A/T/C=-1
for i in range(len(y)):
	if y[i]=='G':
		x.append(1)
	else :
		x.append(-1)
# finding mean and standard deviation
N=len(x)
s=0.0
for i in range(len(x)):
	s+=x[i]
avg=s/N
print avg
stv=0.0
for i in range(len(x)):
	dif=(x[i]-avg)**2
	stv+=dif
stv= stv/N
print stv
# finding corelation
c=[]
k=[]
for i in range(200):
	j=0
	s=0.0
	while j<(len(x)-i):
		s+=(x[j]-avg)*(x[j+i]-avg)
		j+=1
	c.append(s/((N-i)*stv))
	k.append(i)
print c
plot(k,c)
show()
