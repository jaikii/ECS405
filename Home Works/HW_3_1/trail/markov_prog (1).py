import random
import numpy as np
'''
Markov simulation of different order:
..
we have a seq1(current): from that find freq. that is STAT
seq2,seq3 you will get from 3 order markov simulation
Using that make the matrix:
	A	B	C	D	STAT(freq. of seq1 )
A	0.3	0.2	0.4	0.1	0.3	
B	0.5	0.2	0.1	0.2	0.2
C	0.1	0.7	0.2	0.0	0.1
D	0.2	0.2	0.1	0.5	0.4
'''
f=open('markov.py','r')
f.readline()
state=[]
prob=[]
start=[]
for i in f:
	state.append(i.split()[0])
	prob.append(i.split()[1:5])
	start.append(float(i.split()[-1]))
f.close()
#for stationary distribution
print start
n=4
length=input("length of sequence")
p=input("No. of steps")
x=[]
stat=[] #starting dna seq.
def f(start): #to get desired probability list
	x=[]
	for i in range(0,n):
		x+=[i+1 for j in range(int(float(start[i])*10))]
	return x
stat=np.random.choice([1,2,3,4],length,start)
print "1st seq:",stat
F=open("simulated_markov.txt",'w')
for k in stat:
	F.write("%d"%k)
F.write("\n")
for j in range(p-1):
	states=[]
	for i in stat:
		states.append(int(np.random.choice([1,2,3,4],1,prob[i-1])))
	for k in states:
		F.write("%d"%k)
	F.write("\n") 
	stat=states
	print j,": ",states
print "final state:", states
F.close()
'''using that you will get a seq that is the sequence of hidden markov variables (n1,n2,n3)'''
'''Hidden Markov process: we will have emission probability matrix
states:		1	2	3	4	5
hidden state(depends on you):
n1			0.2	0.1	0.1	0.4 0.2
n2			0.4	0.0	0.2	0.1 0.3
n3			0.3	0.5	0.0	0.0	0.2
n4			0.1 0.2 0.4 0.3 0.0
'''
#simulation of hidden markov
def hf(start,k): #to get desired probability list
	x=[]
	for i in range(0,k):
		x+=[i+1 for j in range(int(float(start[i])*10))]
	return x
hprob=[[0.2,0.1,0.1,0.4,0.2],[0.4,0.0,0.2,0.1,0.3],[0.3,0.5,0.0,0.0,0.2],[0.1,0.2,0.4,0.3,0.0]]
hstates=[]
for i in np.array(states):
	hstates.append(np.random.choice([1,2,3,4,5],1,hprob[i-1]))
print "hidden state:",hstates
unique, counts = np.unique(np.array(hstates), return_counts=True)	#counting number of A,T,C,G
dit=dict(zip(unique, counts))
print dit

