#Evolutionary Intelligence: Major Assignment

"""Super Information"""

import numpy as np
from math import *
import random as ra
from matplotlib.pylab import *

#extracting the data from te file
file = open('NC_000964.fna','r')
dna=str()
for f in file:
	a=f.split()
	dna+=a[0]
dna=list(dna)
len_dna=len(dna)
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

#Super Information
def Super_Entropy(dna):
	super_entropy=[]
	for j in range(2,100):
		N=len_dna/j
		H=[]	#entropy of part-wise dna sequence
		for i in range(0,len_dna,N):
			X=dna[i:i+N-1]
			H.append(shannon(X))
		H=H[:-1]
		M1=(max(H)-min(H))*1.0/10		#binning into 50 bins
		M=[]							#probability of each element of H in i'th bin
		for i in range(10):
			temp=0
			for j in H:
				if min(H)+(i+1)*M1 > j > min(H)+(i*M1):
					temp+=1
			M.append(temp*1.0/len(H))  #check
		print M
		s_entropy=0
		for i in M:
			if i!=0.0:
				s_entropy+=-i*log(i)
		print s_entropy
		super_entropy.append(s_entropy)
	return super_entropy
super_entropy=Super_Entropy(dna)
plot(range(len(super_entropy)),super_entropy)
show()
