source VMDextensions.tcl
set seleccio [atomselect top "all"]
renumber_from_1 $seleccio
$seleccio set segname "ION"
$seleccio set chain "I"
set seleccio [atomselect top "name CL"]
$seleccio set name "CLA"
$seleccio set element "CL"
set seleccio [atomselect top "name CS"]
$seleccio set name "CES"
$seleccio set element "CS"
set seleccio [atomselect top "all"]
$seleccio writepdb mymoleculestep2.pdb


