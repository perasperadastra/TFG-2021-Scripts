name=str(input("Filename: "))
#input file
name=name+".xyz"
fin = open(name, "rt")
#output file to write the result to
fout = open("modified.xyz", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
    a=line.replace('Cs', 'CS')
    a=a.replace("Cl", "CL")
    fout.write(a)
#close input and output files
fin.close()
fout.close()
