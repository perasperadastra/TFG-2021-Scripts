value=int(input("Choose the number of files to merge [max=3]\n"))

nam1=str(input("\nInput file name : "))
nam1=nam1+".xyz"
print("\nSecond File: ")
nam2=input("Input file name : ")
nam2=nam2+".xyz"
if value==3:
	print("\nThird File: ")
	nam3=input("Input file name (blabla.what)")
	nam3=nam3+".xyz"
#######################################################################################################
def contadoratomos(name,csNumExtra=0,clNumExtra=0):
	"""
	Function that counts the atoms in our .xyz files.
	"""
	csNum=0+csNumExtra
	clNum=0+clNumExtra
	with open(name,"r") as file1:
			for line in file1:
				if line.startswith("Cs"):
					csNum+=1
				if line.startswith("Cl"):
					clNum+=1
	
	return csNum, clNum

def neutral(name,csNumExtra=0,clNumExtra=0):
	"""
	Function that erase first Cs or Cl till the system is neutralized
	"""
	csNum,clNum=contadoratomos(name,csNumExtra,clNumExtra)
	if csNum==clNum:
		print(" \nWOOOWWWW!!!!!!!\n The total number of atoms are neutral in this merge!!!!!\n")
		return name
	outname=(input("\nOutput file name?: \n")+".xyz")
	out=open(outname,"w")
	csNumOrig=csNum-csNumExtra
	clNumOrig=clNum-clNumExtra
	with open(name,"r") as file1:
		if csNum>clNum:
			diff=csNum-clNum
			out.write(str(clNumOrig+(csNumOrig-diff))+"\n")
			out.write("#   Edited in python :D \n")		
			print("Cs atoms: "+str(csNum)+" -----> "+str(csNum-(csNum-clNum)))
			print("Cl atoms: "+str(clNum)+" -----> "+str(clNum))
			inicio=0
			fileread=file1.readlines()
			for line in fileread:
				inicio+=1
				if inicio<3:
					continue
				difference=int(csNum-clNum)
				if difference>0 and line.startswith("Cs"):
					csNum-=1
					continue
				out.write(line)
		if clNum>csNum:
			diff=clNum-csNum
			out.write(str(clNumOrig+(csNumOrig-diff))+"\n")
			out.write("#   Edited in python :D \n")
			print("Cs atoms: "+str(csNum)+" -----> "+str(csNum))
			print("Cl atoms: "+str(clNum)+" -----> "+str(clNum-(clNum-csNum)))
			incio=0
			for line in file1.readlines():
				inicio+=1
				if inicio<3:
					continue
				difference=int(clNum-csNum)
				if difference>0 and line.startswith("Cl"):
					clNum-=1
					continue
				out.write(line)
	return outname

######################################
#neutralizer
print("\nFile Neutralizer ")
while True:
	decision=input("\n Want to neutralize any file?\n No: 0 \n Yes: 1 \n One repect other: 2 \n" )
	if decision=="0":
		break
	if decision=="1":
		break
	if decision=="2":
		break

while decision=="1" or decision=="2":
	
	if decision=="1":
		while True:
			neutralnam1=input("Neutralize "+nam1+"? [y/n]\n")
			if neutralnam1=="y":
				nam1=neutral(nam1)
			if neutralnam1=="n":
				neutralnam2=input("Neutralize "+nam2+"? [y/n]\n")
				if neutralnam2=="y":
					nam2=neutral(nam2)
				if neutralnam2=="n" and value>2:	
					neutralnam3=input("Neutralize "+nam3+"? [y/n]\n")
					if neutralnam3=="y":
						nam3=neutral(nam3)
					if neutralnam3=="n":
						decision=0
						break
		break
	if decision=="2":
		print("Options:\n"+nam1+" respect "+nam2+" : 0")
		if value>2:
			print(nam1+" respect "+nam3+" : 1")
		print(nam2+" respect "+nam1+" : 2")
		if value>2:
			print(nam2+" respect "+ nam3+" : 3")
			print(nam3+" respect "+ nam1+" : 4")
			print(nam3+" respect "+ nam2+" : 5")
		while True:
			respectdecision=input()			
			if respectdecision=="0" or respectdecision=="1" or respectdecision=="2" or respectdecision=="3" or respectdecision=="4" or respectdecision=="5":
				break
		if respectdecision=="0":
			csNum,clNum=contadoratomos(nam2)
			nam1=neutral(nam1,csNum,clNum)
		if respectdecision=="1":
			csNum,clNum=contadoratomos(nam3)
			nam1=neutral(nam1,csNum,clNum)
		if respectdecision=="2":
			csNum,clNum=contadoratomos(nam1)
			nam2=neutral(nam2,csNum,clNum)
		if respectdecision=="3":
			csNum,clNum=contadoratomos(nam3)
			nam2=neutral(nam2,csNum,clNum)
		if respectdecision=="4":
			csNum,clNum=contadoratomos(nam1)
			nam3=neutral(nam3,csNum,clNum)
		if respectdecision=="5":
			csNum,clNum=contadoratomos(nam2)
			nam3=neutral(nam3,csNum,clNum)
		break





	
	
#####################################################################
file1=open(nam1,"r").readlines()
file2=open(nam2,"r").readlines()
if value==3:
	file3=open(nam3,"r").readlines()
merge=open("merge.xyz","w")

#####################################################################
contador1=-2
contador2=-2
contador3=-2

for line in file1:
	contador1+=1
for line in file2:
	contador2+=1	
if value==3:
	for line in file3:
		contador3+=1
####################################################################
if value==2:
	merge.write(str(contador1+contador2)+"\n")
if value==3:
	merge.write(str(contador1+contador2+contador3)+"\n")
merge.write("#   merge by python"+"\n")

#####################################################################
contador=-1
for line in file1:
	contador+=1
	if contador==0:
		continue
	if contador==1:
		continue
	merge.write(line)
contador=-1
for line in file2:
	contador+=1
	if contador==0:
		continue
	if contador==1:
		continue
	merge.write(line)

if value==3:
	contador=-1
	for line in file3:
		contador+=1
		if contador==0:
			continue
		if contador==1:
			continue
		merge.write(line)


merge.close()
