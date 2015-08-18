## Remove water inside the membrane
## USAGE: vmd -dispdev text -e remove_water_in_membrane.tcl -args \
##   my.psf my.pdb  output_prefix file_str_selection.txt membrane_height 
## AUTHOR: YUHANG WANG 
## DATE: 08/17/2015

proc load {file_psf file_pdb} {
	# load a pair of psf/pdb files 
	# return the VMD molecule ID 
	set molId [mol new $file_psf]
	mol addfile $file_pdb
	return $molId 
}

proc write {molId str_selection output_prefix} {
	# Write the selected atoms into the output psf/pdb files 
	set sel [atomselect $molId $str_selection]
	$sel writepsf ${output_prefix}.psf 
	$sel writepdb ${output_prefix}.pdb 
}

proc get_file_content {file_name} {
	# Read a file
	# Return its content as one string 
	set IN [open $file_name r]
	set content [string trim [read $IN] '\n']
	close $IN 
	return $content
}

proc split_by_space {str_input} {
	# split a string by any number of white spaces
	return [regexp -all -inline {\S+} $str_input]
}

proc remove_water_in_membrane {molId str_selection membrane_height} {
	# recenter the atom selection to the origin
	set sel [atomselect $molId $str_selection]
	set membrane_center [measure center $sel]
	$sel delete
	set membrane_center_z [lindex $membrane_center 2]
	set membrane_z_max [expr $membrane_center_z+$membrane_height/2.]
	set membrane_z_min [expr $membrane_center_z-$membrane_height/2.]

	# return an atom selection string that excludes the water inside the membrane 
	return "not (water and z > $membrane_z_min and z < $membrane_z_max)"
}

proc main {argv} {
	# main function 
	set ccc 0 ;# counter
	set file_psf [lindex $argv $ccc]

	incr ccc
	set file_pdb [lindex $argv $ccc]

	incr ccc
	set output_prefix [lindex $argv $ccc]

	incr ccc
	set file_str_selection [lindex $argv $ccc]

	incr ccc
	set membrane_height [lindex $argv $ccc]

	set str_selection [get_file_content $file_str_selection]
	set molId [load $file_psf $file_pdb]
	set str_selection_no_bad_water [remove_water_in_membrane $molId $str_selection $membrane_height]
	write $molId $str_selection_no_bad_water $output_prefix
}

#=========================================
main $argv; exit;
#=========================================