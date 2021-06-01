struc=open("equil.namd","r")
data=struc.read()
data=data.replace('incr temperature', 'incr pressure')
for line in struc:
    if line.startswith("langevinPistonPeriod"):
        data=data.replace(line, "langevinPistonPeriod  200")
    if line.startswith("langevinPistonDecay"):
        data=data.replace(line, "langevinPistonDecay  100")
struc.close()
struc=open("equil.namd","w")
struc.write(data)
struc.close()
