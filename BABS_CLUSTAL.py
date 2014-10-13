from Bio.SeqUtils import CodonUsage
import os
import sys
# first make a CAI object
X = CodonUsage.CodonAdaptationIndex()
# now generate an index from a file
if os.path.exists("BIN1.fasta"):
	X.generate_index("BIN1.fasta")
elif os.path.exists("BIN1.fasta"):
	X.generate_index("BIN1.fasta")
else:
	print("Cannot find the file BIN1.fasta\nMake sure you run the tests from within the Tests folder")
sys.exit()
# alternatively you could use any predefined dictionary like this:
# from CaiIndices import SharpIndex # you can save your dictionary in this file.
# X.SetCaiIndex(SharpIndex)
print("The current index used:")
X.print_index()
print("-" * 60)
print("codon adaptation index for test gene: %.2f" % X.cai_for_gene("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA"))

