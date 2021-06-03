# TFG-2021-Scripts
This repository contains all the script necesaries to build the pdb and psf file from the atomsk output.

The topology and parameter file belong to CHARMM repository
The VMD

# Building a pdb from xyz file:
0) Copy "editorname.py",step1.tcl","modification_of_pdbfile.tcl","segmentchange.py" and "VMDextensions.tcl" to the working directory.

1) First run the editorname.py file, you must insert the name of the file (without ".xyz") and it will change the name of the ions to be the same as the topology and parameter files.

2) Run VMD and in the TK console "source step1.tcl". || the output file is mymolecule.pdb

3) Add mymoleculestep.pdb as a new molecule and erase all previous molecule in VMD. Then run in the TK console "source modification_of_pdbfile.tcl". Close VMD || The output file is mymoleculestep2.pdb

4) Run segmentchange.py || The output file is mymoleculestep21.pdb

5) NOW THE mymoleculestep21.pdb FILE IS READY 


# Building a psf file
0) Using a correct .pdb file (as the one you can reach with the previous method) open VMD and load this file.

1) Go to Extnsions -> Modeling -> Automatic psf builder

2) Go to step1: Delete all the topology files and load the topology file in this repository

3) Go to step2: Click on "Guess and split chains using current selections" 

4) Go to step3: Click on Create Chains and wait.

5)NOW YOU HAVE THE  mymoleculestep21_autopsf.pdb & mymoleculestep21_autopsf.pdb FILES.

# Using the merger extension
The merger script is used to merge two or three(experimental, you can neutralize the three file independetly, or une file respect other with a third untouch file) xyz files and obtain a neutral system. You can neutralize each file independently or one file respect other, meaning, that if you neutralize FIle1 respect File2, the File1 will lose the necesary ion to be neutral respect the number of ions in File2.
