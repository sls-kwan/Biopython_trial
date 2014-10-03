#this is a python script for finding GC content

gene = open("BIN1.txt", "r")

g=0;
a=0;
c=0;
t=0;\

#skipping header line
gene.readline()

for line in gene:
	line = line.lower
	for char in line:
		if char == "G":
			g+=1
		if char == "A":
			a+=1
		if char == "C":
			c+=1
		if char == "T":
			t+=1
gc = (g+x+0.)/(a+t+c+g+0.)

print "number of gc: " + str(gc)

