def complement(DNA):
	"""
	Converts DNA strand to the complement
	"""
	DNA=DNA.upper()
	DNA=DNA.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
	return DNA
def reverse(complement):
	"""
	Reverts the order of the DNA completementary strand
	"""
	complement=complement.upper()
	return complement[::-1]

DNA=('ATCGTCGCGG')
#to give an example
com=complement(DNA)
rev=reverse(com)
print(rev)
	
