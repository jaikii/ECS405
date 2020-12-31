#Python module to compute the F3 value for a given nucleotide sequence.

def F3(seq):
    l = len(seq)/3
    S = seq[:3*l]       #This is done so that my sequence is a multiple of 3
    s = [S[3*i:3*i+3] for i in range(len(S)/3)]
    s1 = []; s2 = []; s3 = []
    for i in range(len(s)):
        s1.append(s[i][0])
        s2.append(s[i][1])
        s3.append(s[i][2])
    d1 = {x:s1.count(x)*1.0/len(s1) for x in s1}
    d2 = {x:s2.count(x)*1.0/len(s2) for x in s2}
    d3 = {x:s3.count(x)*1.0/len(s3) for x in s3}
    nuc = ['A','T','G','C']
    d = [d1,d2,d3]
    for i1 in d:
        for i2 in nuc:
            if i2 not in i1.keys():
                i1.update({i2:0.0})
    f3 = 0.0
    for n in nuc:
        add = 0.0
        for val in d:
            add += val[n]

        variance = 0.0
        for elem in d:
            variance += (elem[n] - 1.0*add/3)**2
        f3 += variance
    return f3
        
if __name__ == '__main__':
    file = open('/home/iiserb/Downloads/NC_003098.fna','r')
    dna = str()
    for f in file:
        a = f.split()
        dna += a[0]
    dna = list(dna)
    value = F3(dna)
    print value
            
            
            
    
