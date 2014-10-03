#this is a python script for finding GC content
from Bio import SeqIO
from Bio.SeqUtils import GC

dna_sequences = {}
for record in SeqIO.parse("BIN1.txt", "fasta"):
	dna_sequences[record.id] = GC(record.seq)
for a_key, a_value in dna_sequences.iteritems():
	print a_key, a_value
