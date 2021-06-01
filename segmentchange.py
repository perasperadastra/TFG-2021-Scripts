pdb= open("mymoleculestep2.pdb","r")
out=open("mymoleculestep21.pdb","w")
contador=0
for line in pdb:
	contador+=1
	if contador==1:
		out.write(line)
		continue
	if line.startswith("END"):
		out.write(line)
		break
	if contador<=10:
		a=line[21:27]
		line=line.replace(a,"I   "+str(contador-1))
	if contador<=100 and contador>=11:
		a=line[21:27]
		line=line.replace(a,"I  "+str(contador-1))
	if contador<=1000 and contador>=101:
		a=line[21:27]
		line=line.replace(a,"I "+str(contador-1))
	if  contador>=1001:
		a=line[21:27]
		line=line.replace(a,"I"+str(contador-1))
	
	out.write(line)
