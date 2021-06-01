set seleccio [atomselect top "element Cl"]
$seleccio set resname "CLA"
set seleccio [atomselect top "element Cs"]
$seleccio set resname "CES"
set mymolecule [atomselect top "all"]
$mymolecule writepdb mymolecule.pdb
