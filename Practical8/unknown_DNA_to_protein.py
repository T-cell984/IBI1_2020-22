import re
origin=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
protein=''
count=''
file=origin.read()
a=re.split('>',file)
DNA=open('unknown_function.fa','w+')
codon_table={
	'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
	'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
	'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
	'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
	'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
	'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
	'TAT':'Y','TAC':'Y','TAA':'Y','TAG':'U',
	'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
	'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
	'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
	'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
	'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
	'AGT':'S','AGC':'S','AGA':'A','AGG':'R',
	'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
for i in a:
	if 'unknown function' in i:
		genename=re.findall(r'gene:(.+?)\s',i)
		#to get the gene name
		dnaseq=re.sub(r'.+]','',i)
		#to get the DNA sequence
		dnaseq=dnaseq.replace('\n','')
		
		for i in range(0,len(dnaseq),3):
			codon = dnaseq[i:i+3]
			if codon in codon_table:
				protein = protein + codon_table[codon]
				count = len(protein)
			if 'O' in protein:
				break
			if 'U' in protein:
				break
			if 'X' in protein:
				break
			#to stop translation when meeting the termination codon
		DNA.write('\n'+genename[0]+'\t\t\t'+str(count)+'\n')
		DNA.write(protein)
		protein=''
DNA.close()
DNA = open('unknown_function.fa')
print(DNA.read())
DNA.close()
		
			
	
	

