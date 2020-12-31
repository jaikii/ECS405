#Author: Jai Kumar, Roll No.: 15076

from matplotlib.pylab import *
f=open("austen-corpus.txt",'r')
text=''
textarr=[]
for line in f:
	text+=line
f.close()
#Writing into file with all lower characters
k=open("lower-austen-courpus.txt",'w')
k.write(text.lower())
k.close()
punch='''!@#$%^&*()_+}{|":?><-=\][;'/.,`'''
text1=''
for l in text.lower():
	if l in punch:	
		text1+=" "		#So that two words don't mix-up
	else:
		text1+=l

#Count each word and letter
k=open("textwithoutpunctuators.txt",'w')
k.write(text1)
k.close()
f=open("textwithoutpunctuators.txt",'r')
text=[]
for i in f:
	line=i.split()
	text+=line
f.close()
print "Total words: ",len(text)
s=0
wordic={}
letterdic={}
for i in range(len(text)): 	#To give initial values as zero to dictonary elements
	s+=len(text[i])
	wordic[text[i]]=0
	for j in range(len(text[i])):
		letterdic[text[i][j]]=0
for i in range(len(text)): 	#To count
	wordic[text[i]]+=1
	for j in range(len(text[i])):
		letterdic[text[i][j]]+=1
print "Total letters ",s
'''You can print wordic and letterdic to get the frequencies of words and letters'''

#Writing freqency in file
k=open("freq_words.txt",'w')
for i in sorted(wordic.keys()):
	k.write("%s : %d\n"%(i,wordic[i]))
k.close()
k=open("freq_letters.txt",'w')
for i in sorted(letterdic.keys()):
	k.write("%s : %d\n"%(i,letterdic[i]))
k.close()
#Sorting and giving rank to words and letters
A=sorted(wordic, key=wordic.get,reverse=True)
B=sorted(letterdic, key=letterdic.get,reverse=True)
rankword={}
rankletter={}
for i in range(len(A)):		#giving ranks to words
	rankword[i+1]=A[i]
for i in range(len(B)):		#giving ranks to letters
	rankletter[i+1]=B[i]
print "Total distinct words: ",len(wordic)
print "Total distinct letters(including numbers): ",len(letterdic)
#Top five frequent words and letters
print "\nTop five frequent words and letters"
for i in range(1,6):
	print "Rank ",i," ",rankword[i],":",wordic[rankword[i]]," and ",rankletter[i],":",letterdic[rankletter[i]]

x11=sorted(rankword.keys())
y11=sorted(wordic.values(),reverse=True)
x21=sorted(rankletter.keys())
y21=sorted(letterdic.values(),reverse=True)
x12=sorted(log(rankword.keys()))
y12=sorted(log(wordic.values()),reverse=True)
x22=sorted(log(rankletter.keys()))
y22=sorted(log(letterdic.values()),reverse=True)
#Plotting
'''
ylabel("Frequency of words")
xlabel("Rank of words")
plot(x11,y11)
savefig("words.pdf")
show()
ylabel("Frequency of letters")
xlabel("Rank of letters")
plot(x21,y21)
savefig("letter.pdf")
show()
ylabel("log(Frequency of words)")
xlabel("log(Rank of words)")
plot(x12,y12)
savefig("log_words.pdf")
show()
ylabel("log(Frequency of letters)")
xlabel("log(Rank of letters)")
plot(x22,y22)
savefig("log_letter.pdf")
show()
'''
def ext(X):
	s=0.0
	for i in range(len(X)):
		s+=X[i]
	return s/len(X)

#Pearson Coeficient
def cof(x,y):
	ex=ext(x)
	ey=ext(y)
	z=[]
	for i in range(len(x)):
		z.append(x[i]*y[i])
		x[i]=x[i]**2
		y[i]=y[i]**2
	sx=sqrt(ext(x)-(ex**2))
	sy=sqrt(ext(y)-(ey**2))
	exy=ext(z)
	return (exy-(ex*ey)) / (sx*sy)
print "\nPearson correlation coefficient"
print "words:",cof(x11,y11),"\nletters: ",cof(x21,y21),"\nlog_words:",cof(x21,y21),"\nlog_letters: ",cof(x22,y22)
