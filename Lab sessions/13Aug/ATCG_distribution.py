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

N=len(y)
#function to find the distribution
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
		z[i]=z[i]*1.0/N
	return z
A=cot(y,'A')
T=cot(y,'T')
C=cot(y,'C')
G=cot(y,'G')
#summing up all the distances to check
s=0
for i in A.keys():
	s=s+A[i]
	print A[i]
for i in T.keys():
	s=s+T[i]
for i in C.keys():
	s=s+C[i]
for i in G.keys():
	s=s+G[i]
print "Sum= ",s,"\nLength= ",N
#tried to fit the poisson distribution couldn't get it
'''
l=0.5
print l
x=linspace(0,100,101)
#print x
y=[]
for i in range(len(x)):
	ac=float(l**i*e**(-l)/factorial(i))
	y.append(ac)
'''
scatter(A.keys(),A.values(),color='red',label='A')
scatter(T.keys(),T.values(),color='blue',label='T')
scatter(C.keys(),C.values(),color='yellow',label='C')
scatter(G.keys(),G.values(),color='black',label='G')
legend()
show()
def ca(x):
	for i in x.keys():
		x[i]=log(x[i])
	return x
scatter(A.keys(),ca(A).values(),color='red',label='A')
scatter(T.keys(),ca(T).values(),color='blue',label='T')
scatter(C.keys(),ca(C).values(),color='yellow',label='C')
scatter(G.keys(),ca(G).values(),color='black',label='G')
#scatter(x,y,color='green')
legend()
show()
def wri(A):
	F=open("genome.csv",'w')
	for i in A.keys():
		F.write("%d,%f\n"%(i,A[i]))
	F.write("------------------\n")
	F.close()
wri(A)
wri(T)
wri(C)
wri(G)


