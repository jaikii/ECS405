# opening the file to read
F=open("austensense.txt",'r')
l=[]

# reading the file and storing the data in 'l' type array
for line in F:
	lines=line.split()
	l.append(lines)

# reading the no. of times 'the' and 'heaven' is comming in the text
st=0
sh=0
for i in range(len(l)):
	for j in range(len(l[i])):
		if l[i][j]=='the':
			st=st+1
		if l[i][j]=='heaven':
			sh=sh+1
print "The no. of times 'the' and 'heaven' is comming in the text is ",st," and ",sh," respectively"
t=input("press 1 to know the no. of words in each line\npress 2 to get the no. of distinct words in each line")
# to get the total no. of words in each line and full document 
if t==1:
	for i in range(len(l)):
		print i," line has : ",len(l[i])," words"
# to get total distinct words in each line and whole document
# I am using dictonary to get the distinct words out of total by making each word as its index and getting its length at the end    
else:
	A=[]
	if t==2:
		for i in range(len(l)):
			A+=l[i]
			y={}
			for j in range(len(l[i])):
				y[l[i][j]]=0
				print "the %dth line has "%i,len(l[i]),"words and Unique words are ",len(y)
	else:
	        print "please enter the correct choice\n"
x={}
for i in range(len(A)):
	x[A[i]]=0
print "Unique words are ",len(x),"and total number of words are ",len(A)
