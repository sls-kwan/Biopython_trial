#this is a python script for finding GC content
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqUtils import CodonUsage

X = CodonUsage.CodonAdaptationIndex()

dna_sequences = {}
for record in SeqIO.parse("BIN1.fasta", "fasta"):
	dna_sequences[record.id] = GC(record.seq)
for a_key, a_value in dna_sequences.iteritems():
	print a_key, a_value
X.generate_index("sequence.fasta")
X.print_index()

