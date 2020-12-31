#Name- Jai Kumar Roll No. 15076
#Answer for que 2
import numpy as np
F=open("simulate_seq.txt",'r')
seq=[]
for i in F:
	seq.append(list(str(i[:-1])))
#print seq
dic={}
for i in range(4):
	for j in range(4):
		dic["%d_%d"%(i+1,j+1)]=0
unique, counts = np.unique(np.array(seq[0]), return_counts=True)	#counting number of A,T,C,G
dit=dict(zip(unique, counts))
N=int(max(seq[0]))
print "starting probabilities\n"
for i in range(N):
	print i+1," = ",dit["%s"%(i+1)]*1.0/len(seq[0])
for i in range(0,len(seq),2):
	for j in range(len(seq[i])):
		dic["%s_%s"%(seq[i][j],seq[i+1][j])]+= 1.0
tot=[]
for i in range(N):
	s=0.0
	for j in range(int(max(seq[0]))):
		s+=dic["%d_%d"%(i+1,j+1)]
	tot.append(s)
print "probabilities after simulating\n"
for i in range(N):
	for j in range(N):
		print i+1,"->",j+1," = ",dic["%d_%d"%(i+1,j+1)]/tot[i]

		
