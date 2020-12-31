#Name:Jai Kumar Roll. No. 15076
from matplotlib.pylab import *
from math import *
import numpy as np
import glob
 
path = 'DNA/*.fna'   
files=glob.glob(path)
for file in files: #will read all the files from DNA folder
	f=open(file,'r')
	A=[]
	for i in f:
	    l=i.split()
	    A+=l
	B=[]
	for i in range(len(A)):
	    B+=A[i]
	f.close()
	N=len(B)
	print N
	k1=1;x=[];y=[];z=[]
	for i in range(0,N,N/500):
		X=B[i:(i+(N/100))]
		unique, counts = np.unique(np.array(X), return_counts=True)	#counting number of A,T,C,G
		dit=dict(zip(unique, counts))					#making dictonary of the count
		t=(1.0*(dit['G']-dit['C']))/(dit['G']+dit['C'])			#CG_skew  
		##Corelation function
		S=[1 if X[i]=='G' else -1 for i in range(len(X))]
		Ns=len(S)
		cg=0.0
		for k in range(1,20):
			ck=0.0
			for j in range(1,Ns-k):
				ck+=1.0*S[j]*S[j+k]
			cg+=abs(ck)/(30*(Ns-k))
		z.append(cg)
		x.append(k1)
		y.append(t)
		k1+=1
	plot(x,y,label='CG_skew')
	xlabel("ith sequence(of length %d)"%(N/100))
	ylabel("CG_skew/Correlation")	
	plot(x,z,label='Correlation')
	legend()
	savefig("%s_1.pdf"%file)
	show()
