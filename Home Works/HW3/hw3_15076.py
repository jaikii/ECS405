#Name: Jai Kumar RollNo. 15076
import math
gene=[]
seq=[]
f=open("Homo_sapiens.GRCh38.cds.all.fa",'r')
seq1=str()
z=0

###### Extracting the data from file to 'seq[i]' array ######
for i in f:
	t=0
	if i.startswith('>'):
		gene.append(i.split()[0][1:]) #making array to store the gene number
		t+=1
		if z>=1:
			seq.append(seq1)
			z=0
			seq1=str()
	else:
		if t==0:
			seq1+=str(i[:-1])
			z+=1

###### Storing standard coding table in a dictionary #####
dic={}
dicA={}
sq=[]
A='TCAG'
for i in range(len(A)):
	for j in range(len(A)):
		for k in range(len(A)):
			dic['%s%s%s'%(A[i],A[j],A[k])]=0
			sq.append('%s%s%s'%(A[i],A[j],A[k]))
ncbi = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i in range(len(ncbi)):
	dic[sq[i]]=ncbi[i]
	dicA[ncbi[i]]=0

##### Converting DNA to Protein #####
AA=[]
for i in range(len(seq)):
	AA1=str()
	for j in range(0,len(seq[i]),3):
		if j <=len(seq[i])-1 and j+1 <=len(seq[i])-1 and j+2 <=len(seq[i])-1 and seq[i][j]!='N' and seq[i][j+1]!='N' and seq[i][j+2]!='N':	#since there are sequences with 'N' in it so, i skipped the codons including 'N' in it 
			C="%s%s%s"%(seq[i][j],seq[i][j+1],seq[i][j+2])	
			#print C
			AA1+=str(dic[C])
	AA.append(AA1)				# AA[i] has the amino acid sequence of each gene
AF=[]
for i in range(len(AA)):
	L=dict.fromkeys(dicA.iterkeys(), 0)
	for j in AA[i]:
		L[j]+=1.0/len(AA[i])
	AF.append(L)				# Array of dictonaries having freq. of aminoacid

###### To find Mean of each amino acid in all genes (taking sum of frequency of an amino acid in all the gene and divide by total genes) ######
dicM={}			
for i in dicA.keys():
	s=0
	for j in range(len(AF)):
		s+=AF[j][i]
	dicM[i]=s/len(AF)
print "Mean:\n",dicM					# Dictonary having mean 

##### To find Standard Deviation #####
dicS={}
for i in dicA.keys():
	s=0
	for j in range(len(AF)):
		s+=(dicM[i]-AF[j][i])**2
	dicS[i]=s**(1/2)/len(AF)
print "Standard Deviation: \n",dicS					# Dictonary having Standard deviation
print "DNA seq:\n",seq[len(seq)-1],"\nAmino Acid Sequence:\n",AA[len(seq)-1],"\nAmino Acid frequency:\n",AF[len(seq)-1]
