#this is a python script for finding GC content
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.SeqUtils import CodonUsage
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Align.Applications import ClustalOmegaCommandline
#import packages 

dna_sequences = {} #create dictionary 
for record in SeqIO.parse("BIN1.fasta", "fasta"): #parse file into record 
	dna_sequences[record.id] = GC(record.seq) #initialise dictionary id and GC value 
for a_key, a_value in dna_sequences.iteritems(): #prints corresponding id file with GC content
	print a_key, a_value

input_handle = open("sequence.gb", "rU") #opens file
output_handle = open("BIN1.fasta", "w") #open file for writing

sequences = SeqIO.parse(input_handle, "genbank") #parse file to sequence type
count = SeqIO.write(sequences, output_handle, "fasta") #write to file from sequence type

output_handle.close() #closes filehandlers
input_handle.close()

output_handle = open("BIN1.fastaq", "a") #open file for appending
dna_seq = {}
for record in SeqIO.parse("BIN1.fasta", "fasta"):
	seq = Seq(str(record.seq), generic_dna)  #record.seq gets sequence, parsed to string to allowed it to be stored as Seq type
	dna_seq[record.id] = seq.complement()  #generates complementary for each id sequence
	b = record.description + 'Complement'  #appends complement to description of sequence
	a = SeqRecord(seq, record.id, record.name, b) #make seqrecord type then appends to file that has been opened
	SeqIO.write(a, output_handle, "fasta")  
for a_key, a_value in dna_seq.iteritems():
	print a_key, a_value

first_input = open("BIN1.fasta", "rU")  #first input
second_input = open("sequence.fasta", "a") #second input opened to append mode

multi_seq = SeqIO.parse(first_input, "fasta")  
multi_seq1 = SeqIO.write(multi_seq, second_input, "fasta") 
first_input.close()
second_input.close()

in_align = "sequence.fasta"
out_align = "aligned.fasta"
clustalomega_cline = ClustalOmegaCommandline(infile=in_align, outfile=out_align, verbose=True, auto=True, force=True) #creates CLustalOmega command, forcing true to overwrite file
clustalomega_cline()  #executes command

