#Author: Jai Kumar Roll No.: 15076

from matplotlib.pylab import *
from math import *
'''It gives corelation of Parts of DNA sequence cutting it in length N/100 after N/500th Base Then finding segment no.: (#G-#C)/(#G+#C)
	Corelation: C(k)=1/(Ns-K) * sum(1,Ns-k) Aj.Aj+k
	 	    Cg= 1/Ns-1 * sum(1,Ns-1) C(k)
	Kink will show the origin of Replication
'''
'''
# pearson coefficient
def ext(X):
	s=0.0
	for i in range(len(X)):
		s+=X[i]
	return s/len(X)

def cof(x,y):
	ex=ext(x)
	ey=ext(y)
	z=[]
	x1=[]
	y1=[]
	for i in range(len(x)):
		z.append(x[i]*y[i])
		x1.append(x[i]**2)
		y1.append(y[i]**2)
	sx=sqrt(ext(x1)-(ex**2))
	sy=sqrt(ext(y1)-(ey**2))
	exy=ext(z)
	return (exy-(ex*ey)) / (sx*sy)
'''
def cout(B):
	dict={}
	for i in B:
		if i in dict.keys():
			dict[i]+=1
		else:
			dict[i]=1
	return dict
#reading dna sequence
f=open('DNA_Seq/NC_000964.fna','r')
A=[]
for i in f:
    l=i.split()
    A+=l
B=[]
for i in range(len(A)):
    B+=A[i]
f.close()
f=open("out_dna_seq.txt",'w')
N=len(B)
print N
k1=1
x=[]
y=[]
z=[]
for i in range(0,N,N/500):
	X=B[i:(i+(N/100))]
	dit= cout(X)
	t=(1.0*(dit['G']-dit['C']))/(dit['G']+dit['C'])
	#f.write("%d %f\n"%(k,t))
	S=[]
	for i in range(len(X)):
		if X[i]=='G':
			S.append(1)
		else:
			S.append(-1)
	Ns=len(S)
	cg=0.0

	#Corelation function
	for k in range(1,30):
		ck=0.0
		for j in range(1,Ns-k):
			ck+=1.0*S[j]*S[j+k]
		cg+=abs(ck)/(30*(Ns-k))
	print cg,"\n"
	x.append(k1)
	y.append(t)
	z.append(cg)
	k1+=1	
f.close()
plot(x,y)
xlabel("Segment no.")
ylabel("Value")
plot(x,z)
show()
'''
f=open("keratin.fasta",'r')
f.readline()
A=[]
for i in f:
    l=i.split()
    A+=l
B=[]
for i in range(len(A)):
    B+=A[i]
f.close()
D=[]
for i in range(0,len(B),3):
    C= "%s%s%s"%(B[i],B[i+1],B[i+2])
    D.append(C)

#making dictonary for ATCG
dic={}
sq=[]
A='TCAG'
for i in range(len(A)):
	for j in range(len(A)):
		for k in range(len(A)):
			dic['%s%s%s'%(A[i],A[j],A[k])]=0
			sq.append('%s%s%s'%(A[i],A[j],A[k]))

#reading codon table
ct=[]
t1=[]
f=open("codontable.txt",'r')
for l in f:
	l1=l.split()
	ct1=[]
	t=0
	if len(l1)>0:
		if l1[0]=='id':
			t1.append(l1[1])
		if l1[0]=='ncbieaa':
			ct1.append(t1)
			ct1.append(l1[1][1:-2])
			t+=1
		if t!=0:
			ct.append(ct1)
#print ct
pro=[]
#translating for protein
for i in range(len(ct)):
	pro1=[]
	for j in range(len(ct[i][1])):
		dic[sq[j]]=ct[i][1][j]
	pro1.append(ct[i][0])
	for k in range(len(D)):
		pro1.append(dic[D[k]])
	pro.append(pro1)
#printing protein sequence
'''
'''
for i in range(len(pro)):
	for j in range(len(pro[i])):
		print pro[i][j],
	print "\n"
'''
'''
print len(pro[1])
AA=[]
for i in range(len(pro)):
	adic={}
	for j in range(1,len(pro[i])):
		if pro[i][j] in adic.keys():
			adic[pro[i][j]]+=1
		else:
			adic[pro[i][j]]=1
	AA.append(adic)
#Finding corelation between the codon table
aa="CWLPHQRIMTNKVADEGFSY*"
aaa=[aa[i] for i in range(len(aa))] 
aas=[]
#print AA
for i in range(len(AA)):
	aas1=[]
	#print t1[i],":",
	for j in (aaa):
		if j in AA[i]:
			aas1.append(AA[i][j])
			#print AA[i][j],
		else :
			aas1.append(0)
			#print 0
	#print "\n"
	aas.append(aas1)
print"  ",
for i in range(1,len(t1)):
	print " %d "%int(t1[i]),
print "\n"
for i in range(len(aas)-1):
	print t1[i],":",
	for j in range(i+1,len(aas)):
		x=aas[i]
		y=aas[j]
		#print t1[i],t1[j]," : ",
		print "%0.2f"%cof(x,y),
	print "\n"
'''
