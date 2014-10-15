#this is a python script for finding GC content
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.SeqUtils import CodonUsage
from Bio.Alphabet import generic_dna, generic_protein

dna_sequences = {}
for record in SeqIO.parse("BIN1.fasta", "fasta"):
	dna_sequences[record.id] = GC(record.seq)
for a_key, a_value in dna_sequences.iteritems():
	print a_key, a_value

input_handle = open("sequence.gb", "rU")
output_handle = open("BIN1.fasta", "w")

sequences = SeqIO.parse(input_handle, "genbank")
count = SeqIO.write(sequences, output_handle, "fasta")

output_handle.close()
input_handle.close()

dna_seq = {}
for record in SeqIO.parse("BIN1.fasta", "fasta"):
	seq = Seq(str(record.seq), generic_dna)
	dna_seq[record.id] = seq.complement()
for a_key, a_value in dna_seq.iteritems():
	print a_key, a_value

