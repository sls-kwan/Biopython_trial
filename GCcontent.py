#this is a python script for finding GC content

gene = open("BIN1.txt", "r")

g=0;
a=0;
c=0;
t=0;\

#skipping header line
gene.readline()

for line in gene:
	line = line.lower()
	for char in line:
		if char == "g":
			g+=1
		if char == "a":
			a+=1
		if char == "c":
			c+=1
		if char == "t":
			t+=1
gc = (g+c+0.) / (a+t+c+g+0.)

print "number of gc: " + str(gc)

