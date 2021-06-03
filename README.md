# TFG-2021-Scripts
This repository contains all the script necesaries to build the pdb and psf file from the atomsk output.

# Building a pdb and psf from xyz file:
0)Copy "editorname.py",step1.tcl","modification_of_pdbfile.tcl","segmentchange.py" and "VMDextensions.tcl" to the working directory.

1) First run the editorname.py file, you must insert the name of the file (without ".xyz") and it will change the name of the ions to be the same as the topology and parameter files.

2) Run VMD and in the TK console "source step1.tcl". || the output file is mymolecule.pdb

3) Add mymoleculestep.pdb as a new molecule and erase all previous molecule in VMD. Then run in the TK console "source modification_of_pdbfile.tcl". Close VMD || The output file is mymoleculestep2.pdb
