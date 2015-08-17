## Recenter the input molecule
# Yuhang Wang
# 06/10/2015

set ccc 0
set in_psf [lindex $argv $ccc]
incr ccc
set in_pdb [lindex $argv $ccc]
incr ccc
set out_prefix [lindex $argv $ccc]

set molId [mol new $in_psf]
mol addfile $in_pdb molid $molId 

# re-center
set all [atomselect $molId all]
$all moveby [vecinvert [measure center $all]]

animate write psf ${out_prefix}.psf 
animate write pdb ${out_prefix}.pdb
exit