import numpy as np
F=open("simulated_markov.txt",'r')
seq=[]
for i in F:
	seq.append(list(str(i[:-1])))
#print seq
dic={}
for i in range(4):
	for j in range(4):
		dic["%d_%d"%(i+1,j+1)]=0
sorted(dic)
print dic,len(seq)
unique, counts = np.unique(np.array(seq[0]), return_counts=True)	#counting number of A,T,C,G
dit=dict(zip(unique, counts))
sorted(dit)
print dit
for i in range(0,len(seq),2):
	for j in range(len(seq[i])):
		dic["%s_%s"%(seq[i][j],seq[i+1][j])]+= 1.0
tot=[]
for i in range(4):
	s=0.0
	for j in range(4):
		s+=dic["%d_%d"%(i+1,j+1)]
	tot.append(s)
for i in range(4):
	for j in range(4):
		dic["%d_%d"%(i+1,j+1)]=dic["%d_%d"%(i+1,j+1)]/tot[i]
sorted(dic)
print dic

		
