import re
file1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2=open('unknown_function.fa','w')
file_read=file1.read()
x=re.split('>',file_read)
#to make the sentence more like a list
for i in x:
	if 'unknown function' in i:
		a=re.findall(r'gene:(.+?)\s',i)
		#to get the gene name
		dnaseq=re.sub(r'.+]','',i)
		#to get the DNA sequence
		b=re.sub(r'\n','',dnaseq)
		c=len(b)
		#to count the length of DNA sequence
		for d in a:
			file2.write(d)
			file2.write('\t\t\t')
			file2.write(str(c))
			file2.write(dnaseq)

file1.close()
file2.close()
file2 = open('unknown_function.fa')
print(file2.read())
file2.close()
			
