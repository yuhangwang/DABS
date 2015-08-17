#========================================================
# >>>>>>>>>>>>> ionize <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Yuhang Wang
# 06/10/15
# usage: vmde add_ion.tcl -args my.psf my.pdb my_out_prefix SOD CLA [salt concentration mol/L]

package require autoionize

set ccc 0
set in_psf [lindex $argv $ccc]
incr ccc
set in_pdb [lindex $argv $ccc]
incr ccc
set output_prefix [lindex $argv $ccc]
incr ccc
set cation [lindex $argv $ccc]
incr ccc
set anion [lindex $argv $ccc]
incr ccc
set ion_concentration [lindex $argv $ccc]

set min_dist_from_solute 5
set min_dist_between_ions 5
set ion_segn "ION"
autoionize -psf $in_psf -pdb $in_pdb -sc $ion_concentration -cation $cation -anion $anion -o  $output_prefix -from $min_dist_from_solute -between $min_dist_between_ions -seg $ion_segn


exit
