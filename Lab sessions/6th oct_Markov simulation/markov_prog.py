import random
import numpy as np
'''
Markov simulation of different order:

we have a seq1(current): from that find freq. that is STAT
seq2,seq3 you will get from 3 order markov simulation
Using that make the matrix:
	A(	B	C	D	STAT(freq. of seq1 )
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
	start.append(i.split()[-1])
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
for i in range(length):
	stat.append(random.choice(f(start)))
print "1st seq:",stat
for j in range(10):
	states=[]
	for i in stat:
		states.append(random.choice(f(prob[i-1])))
	print j,": ",states
'''Hidden Markov process: we will have emission probability matrix
states:		1	2	3	4	5
hidden state(depends on you):
n1		0.2	0.3
n2
n3

'''
