f=open("sequence.fasta",'r')
f.readline()
A=[]
for i in f:
    l=i.split()
    A+=l
B=[]
for i in range(len(A)):
    B+=A[i]
'''
for i in range(len(B)):
    if B[i]=='T':
        B[i]='U'
'''
#print B
dic={}
f.close()
f=open("hu.txt",'r')
for i in f:
    l=i.split()
    k=l[1].split(",")
    for j in range(len(k)):
        dic[k[j]]=l[0]
print dic
f.close()
f=open("protein.txt",'w')
i=0
D=[]
while i<len(B):
    C= "%s%s%s"%(B[i],B[i+1],B[i+2])
    D.append(C)
    i+=3
for i in range(len(D)):
    f.write("%s"%dic[D[i]])
    print dic[D[i]]
f.close()
