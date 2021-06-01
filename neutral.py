
name=input("Input file name: \n")

outname=input("\nOutput file name?: \n")
out=open(outname+".xyz","w")
csNum=0
clNum=0

with open(name+".xyz","r") as struct:
	for line in struct:
		if line.startswith("Cs"):
			csNum+=1
		if line.startswith("Cl"):
			clNum+=1

with open(name+".xyz","r") as struct:
	if csNum>clNum:
		out.write(str(clNum*2)+"\n")
		out.write("#   Edited in python :D \n")		
		print("Cs atoms: "+str(csNum)+" -----> "+str(csNum-(csNum-clNum)))
		print("Cl atoms: "+str(clNum)+" -----> "+str(clNum))
		inicio=0
		for line in struct.readlines():
			inicio+=1
			if inicio<3:
				continue
			difference=int(csNum-clNum)
			if difference>0 and line.startswith("Cs"):
				csNum-=1
				continue
			out.write(line)
	if clNum>csNum:
		out.write(str(clNum*2)+"\n")
		out.write("#   Edited in python :D \n")
		print("Cs atoms: "+str(csNum)+" -----> "+str(csNum))
		print("Cl atoms: "+str(clNum)+" -----> "+str(clNum-(clNum-csNum)))
		incio=0
		for line in struct:
			inicio+=1
			if inicio<3:
				continue
			difference=int(clNum-csNum)
			if difference>0 and line.startswith("Cl"):
				clNum-=1
				continue
			out.write(line)
