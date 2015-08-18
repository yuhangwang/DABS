#========================================================
# >>>>>>>>>>>>> solvate <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Yuhang Wang
# 06/10/15
# usage: vmd -dispdev text -e add_water.tcl -args \
# my.psf my.pdb my_out_prefix 100 100 100 [z offset] [min distance between water and solute]
#========================================================

package require solvate
set ccc 0
set in_psf [lindex $argv $ccc]
incr ccc
set in_pdb [lindex $argv $ccc]
incr ccc
set output_prefix [lindex $argv $ccc]
incr ccc
set Lx [lindex $argv $ccc]
incr ccc
set Ly [lindex $argv $ccc]
incr ccc
set Lz [lindex $argv $ccc]

incr ccc
if {[llength $argv ] > $ccc} {
	set z_offset [lindex $argv $ccc]
} else {
	set z_offset 0
}

incr ccc
if {[llength $argv] > $ccc } {
	set min_dist_between_water_solute [lindex $argv $ccc]
} else {
	# use default 
	set min_dist_between_water_solute 2.4
}

set xmin [expr -$Lx/2.0]
set ymin [expr -$Ly/2.0]
set zmin [expr -$Lz/2.0 + $z_offset]
set xmax [expr  $Lx/2.0]
set ymax [expr  $Ly/2.0]
set zmax [expr  $Lz/2.0 + $z_offset]

set list_min [list $xmin $ymin $zmin]
set list_max [list $xmax $ymax $zmax]
set list_minmax [list $list_min $list_max]

solvate $in_psf $in_pdb -o  $output_prefix -b $min_dist_between_water_solute -minmax $list_minmax


exit
