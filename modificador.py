#este formato ya es funcional
txt=open("equil.namd","r")
data=txt.readlines()
contador=-1
for line in data:
   contador=contador+1
   #if line.startswith("outputName"):
   #   data[contador]="#"+line
   #   print("coincidence 1")
   if line.startswith("    run"):
      data[contador]="  run 100000\n}"
      print("conincidence 2")
   #if line.startswith("dcdfreq"):
      #data[contador]="dcdfreq             10000     ;# 500steps = 1 ps \nxstFreq             1000 \noutputEnergies             250\n"
      #print("coincidence 3")
   #if line.startswith("xstfreq"):
   #   data[contador]="xstFreq             1000"
   #   print("coincidence 3")
txt.close()
txt=open("equil.namd","w")
txt.writelines(data)
txt.close()
