#Evolutionary Intelligence: Major Assignment

"""Super Information"""

from matplotlib.pylab import *
from math import *
import cmath
import numpy as np
import random as rm
import glob

#extracting the data from te file
path = 'DNA/*.fna'   
files=glob.glob(path)
for file in files:
	F = open(file,'r')
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

	#finding the frequency
	def freq(dna):
		unique, counts=np.unique(np.array(dna),return_counts=True)
		freq_dna=dict(zip(unique,counts*1.0/len(dna)))
		return freq_dna

	#finding the Shannon Entropy
	def shannon(dna):
		freq_dna=freq(dna)
		Shannon_Entropy=0
		for i in freq_dna.keys():
			Shannon_Entropy+=-freq_dna[i]*log(freq_dna[i])
		return Shannon_Entropy

	#shuffling the dna sequence to show shannon entropy doesn't depend on the order
	'''dna1=dna;ra.shuffle(dna1);dna2=dna;ra.shuffle(dna2);dna3=dna;ra.shuffle(dna3)
	print shannon(dna1),shannon(dna2),shannon(dna3)'''

	#ra.shuffle(dna)
	def val(dna,nucl):
		dna1=[1 if i==nucl else 0 for i in dna]
		return dna1

	#Super Information
	def Super_Entropy(dna):
		super_entropy=[]
		for j in range(2,100):
			N=len_dna/j
			H=[]	#entropy of part-wise dna sequence
			len_X=len(dna[0:N-1])
			for i in range(0,len_dna,N):
				X=dna[i:i+N-1]
				if len(X)>=len_X:
					len_X=len(X)
					H.append(shannon(X))
			#scatter(range(len(H)),H)
			#show()
			#H=H[:-3]
			#scatter(range(len(H)),H)
			#show()
			M1=(max(H)-min(H))*1.0/10		#binning into 50 bins
			M=[]							#probability of each element of H in i'th bin
			for i in range(10):
				temp=0
				for j in H:
					if min(H)+(i+1)*M1 >= j >= min(H)+(i*M1):
						temp+=1
				M.append(temp*1.0/len(H))  #check
			#print M
			s_entropy=0
			for i in M:
				if i!=0.0:
					s_entropy+=-i*math.log(i,10)
			print s_entropy
			super_entropy.append(s_entropy)
		return super_entropy

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
		#print len(S_),t11						#P value
		return t11

	P_value_coding=[];P_value_non_coding=[]
	dna_coding=[]		#all coding region in one
	dna_non_coding=[]
	for i in range(len(coding)):
		P_value_coding.append(P(dna[coding[i][0]-1:coding[i][1]]))
		dna_coding+=dna[coding[i][0]-1:coding[i][1]]
		if i==0:
			dna_non_coding+=dna[0:coding[i][0]]
			if len(dna[0:coding[i][0]])>50:
				P_value_non_coding.append(P(dna[0:coding[i][0]]))
		if i!=0 and i<len(coding)-1:
			dna_non_coding+=dna[coding[i][1]:coding[i+1][0]]
			if len(dna[coding[i][1]:coding[i+1][0]])>50:
				P_value_non_coding.append(P(dna[coding[i][1]:coding[i+1][0]]))
		if i==len(coding)-1:
			dna_non_coding+=dna[coding[i][1]:len(dna)]
			if len(dna[coding[i][1]:len(dna)])>50:
				P_value_non_coding.append(P(dna[coding[i][1]:len(dna)]))
	print len(dna_coding),len(dna_non_coding)
	#print dna_
	##plotting P-value for coding and non-coding
	title(file)
	plot(range(len(P_value_coding)),[4 for i in range(len(P_value_coding))],color='black')
	scatter(range(len(P_value_coding)),P_value_coding,color='red',label='coding')
	scatter(range(len(P_value_non_coding)),P_value_non_coding,color='blue',label='non_coding')
	legend()
	show()

	##plotting Super entropy for coding and non-coding
	title(file)
	super_entropy_coding=Super_Entropy(dna_coding)
	super_entropy_non_coding=Super_Entropy(dna_non_coding)
	plot(range(len(super_entropy_coding)),super_entropy_coding,color='red',label='coding')
	plot(range(len(super_entropy_non_coding)),super_entropy_non_coding,color='blue',label='non_coding')
	legend()
	show()
