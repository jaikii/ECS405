#Author: Jai Kumar Roll No.: 15076

from matplotlib.pylab import *
from math import *
import cmath
import numpy as np
import random
'''	GENETIC ALGORITHM :
	Fitness Function: We are trying to maximize P(=S(N/3)/Savg) value can be done by mutation or cross over
			parent seq------to--- daughter p=P/4 taking generation to (1000) fixed
'''

def fitness(S):
	#mutation
	for i in range(len(S)):
		for j in range(10):
			n=random.randint(0,len(S[i])-1)
			n1=random.random()
			if n1>0.5:
				if S[i][n]==0:
					S[i][n]=1
				else:
					S[i][n]=0
	S_=[]
	#cross-over
	for i in range(len(S)-1):
		A1=S[i][len(S[i])/2:]
		A2=S[i][:len(S[i])/2]
		B1=S[i+1][len(S[i+1])/2:]
		B2=S[i+1][:len(S[i+1])/2]
		A11=A1+B1
		A12=A1+B2
		A13=B2+A1
		A14=B1+A1
		A21=A2+B1
		A22=A2+B2
		A23=B2+A2
		A24=B1+A2
		S_.append(A11);S_.append(A12);S_.append(A13);S_.append(A14);S_.append(A21);S_.append(A22);S_.append(A23);S_.append(A24)
	return S_

S=[]
for j in range(1000): 
	c=[random.random() for l in range(2**(10))]
	S1=[1 if k<=1.0/3 else 0 for k in c]
	FT=abs(np.fft.fft(S1))
	s.append(FT[(len(FT)/3)-1]/mean(FT))
	S.append(S1)
print len(S),len(S[0])
def frac(s):
	t=0.0
	for i in range(len(s)):
		if s[i]>2:
			t+=1
	t1= t*1.0/len(s)
	return (t1)
t1=frac(s)
a=t1
print t1
k=0.0
t=[]
##Iterarting 
while k<100:
	S_=fitness(S)
	s=[]
	Snew=[]
	i=j=0
	t111=0
	while i <(len(S_)) and j<1000:
		FT=abs(np.fft.fft(S_[i]))
		t11=FT[(len(FT)/3)-1]*1.0/mean(FT)			#P value
		s.append(t11)
		if 10*random.random()<t11<4.0:				#selecting sequences out of 8000
			Snew.append(S_[i])
			t111+=t11
			j+=1
		i+=1
	k+=1
	S=Snew
	t1=frac(s)
	t.append(t111*1.0/1000)						#average P value
	x.append(k)
scatter(x,t)
xlabel("No. of iterations")
ylabel("mean P value")
savefig("que_3.pdf")
show()

