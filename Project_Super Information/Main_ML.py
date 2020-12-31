#Evolutionary Intelligence: Major Assignment
#Author: Jai Kumar(15076) & Manav Mishra(15206)
"""Super Information"""

from matplotlib.pylab import *
from math import *
import cmath
import numpy as np
import random as ra
import glob
from F3 import F3
#extracting the data from te file
path = 'DNA/*.fna'   
files=glob.glob(path)
for file in files:
	F = open(file,'r')
	print (file," START")
	dna=str()
	for f in F:
		a=f.split()
		dna+=a[0]
	dna=list(dna)
	len_dna=len(dna)
	F.close()

	#extracting data from .gff3 file
	F=open("%s.gff3"%file[:-4],'r')
	coding=[]
	for i in F:
		k=i.split()
		if len(k)>=3:
			if k[2]=='gene':
				coding.append([int(k[3]),int(k[4])])
	F.close()

	##finding the frequency
	def freq(dna):
		unique, counts=np.unique(np.array(dna),return_counts=True)
		freq_dna=dict(zip(unique,counts*1.0/len(dna)))
		return freq_dna

	##finding the Shannon Entropy
	def shannon(dna):
		freq_dna=freq(dna)
		Shannon_Entropy=0
		for i in freq_dna.keys():
			Shannon_Entropy+=-freq_dna[i]*log(freq_dna[i])
		return Shannon_Entropy


	def val(dna,nucl):
		dna1=[1 if i==nucl else 0 for i in dna]
		return dna1

	##Super Information
	def Super_Entropy(dna):			#at B=90
		N=20
		H=[]				#entropy of part-wise dna sequence
		for i in range(0,len_dna,N):
			X=dna[i:i+N]
			if len(X)==N:
				H.append(shannon(X))
		data = np.array(H)
		M , edges = np.histogram(data, bins=10)
		M= M*1.0/len(H)
		s_entropy=0
		for i in M:
			if i!=0.0:
				s_entropy+=-i*math.log(i,2)
		return s_entropy

	## P-value calculation
	def P(S_):
		S1=val(S_,'A')
		S2=val(S_,'T')
		S3=val(S_,'C')
		S4=val(S_,'G')
		Xk1=abs(np.fft.fft(S1))
		Xk2=abs(np.fft.fft(S2))
		Xk3=abs(np.fft.fft(S3))
		Xk4=abs(np.fft.fft(S4))
		Xk=[]
		for j in range(len(Xk1)):
			Xk.append(Xk1[j]**2+Xk2[j]**2+Xk3[j]**2+Xk4[j]**2)
		t11=Xk[(len(Xk)+1)/3]*1.0/mean(Xk)
		return t11
	F=open("MLinput.txt",'a')
	P_value_coding=[];P_value_non_coding=[]
	Hs_coding=[];Hs_non_coding=[]
	F3_coding=[];F3_non_coding=[]
	#F.write("P_value,Super_entropy,F3,Coding/non_coding\n")
	j=0
	for i in range(len(coding)):
		P_value_coding.append(P(dna[coding[i][0]-1:coding[i][1]]))
		Hs_coding.append(Super_Entropy(dna[coding[i][0]-1:coding[i][1]]))
		F3_coding.append(F3(dna[coding[i][0]-1:coding[i][1]]))
		F.write("%0.5f,%0.5f,%0.5f,'coding'\n"%(P_value_coding[i],Hs_coding[i],F3_coding[i]))
		if i==0:
			if len(dna[0:coding[i][0]])>50:
				P_value_non_coding.append(P(dna[0:coding[i][0]]))
				Hs_non_coding.append(Super_Entropy(dna[0:coding[i][0]]))
				F3_non_coding.append(F3(dna[0:coding[i][0]]))
				#Hs_coding.append(Super_Entropy(dna[coding[i][0]-1:coding[i][1]]))
				F.write("%0.5f,%0.5f,%0.5f,'non_coding'\n"%(P_value_non_coding[j],Hs_non_coding[j],F3_non_coding[j]))
				j+=1
		if i!=0 and i<len(coding)-1:
			if len(dna[coding[i][1]:coding[i+1][0]])>50:
				P_value_non_coding.append(P(dna[coding[i][1]:coding[i+1][0]]))
				Hs_non_coding.append(Super_Entropy(dna[coding[i][1]:coding[i+1][0]]))
				F3_non_coding.append(F3(dna[coding[i][1]:coding[i+1][0]]))
				F.write("%0.5f,%0.5f,%0.5f,'non_coding'\n"%(P_value_non_coding[j],Hs_non_coding[j],F3_non_coding[j]))
				j+=1
				#Hs_coding.append(Super_Entropy(dna[coding[i][0]-1:coding[i][1]]))
		if i==len(coding)-1:
			if len(dna[coding[i][1]:len(dna)])>50:
				P_value_non_coding.append(P(dna[coding[i][1]:len(dna)]))
				Hs_non_coding.append(Super_Entropy(dna[coding[i][1]:len(dna)]))
				F3_non_coding.append(F3(dna[coding[i][1]:len(dna)]))
				F.write("%0.5f,%0.5f,%0.5f,'non_coding'\n"%(P_value_non_coding[j],Hs_non_coding[j],F3_non_coding[j]))
				j+=1
				#Hs_coding.append(Super_Entropy(dna[coding[i][0]-1:coding[i][1]]))
	#print Hs_coding,Hs_non_coding
	#scatter(P_value_coding,F3_coding,color='red',label='coding')
	#scatter(range(len(F3_non_coding)),F3_non_coding,color='blue',label='non-coding')
	#legend()
	#savefig("Hs%s.pdf"%file[-4])
	print (file," DONE")
	show()
	
