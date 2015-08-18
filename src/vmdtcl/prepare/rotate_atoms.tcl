## rotate an atom selection 
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

proc get_rotation_parameter_list {file_name} {
	# get a list of rotation parameters 
	# e.g. {{x 100} {y 90} {z 180}}
	set IN [open $file_name r]
	set lines [split [read $IN] "\n"]
	set list_output {}
	foreach line $lines {
		lassign [split_by_space $line] which_axis rotation_degrees
		lappend list_output [list $which_axis $rotation_degrees]
	}
	close $IN 
	return $list_output
}

proc recenter {molId str_selection} {
	# recenter the atom selection to the origin
	set sel [atomselect $molId $str_selection]
	set old_center [measure center $sel]
	$sel moveby [vecinvert [measure center $sel]]
	set new_center [measure center $sel]
	puts "old center $old_center"
	puts "new center $new_center"
}


proc rotate_atoms {molId str_selection which_axis rotation_degrees} {
	# move selected atoms by {dX dY dZ}
	puts "Rotate around \"$which_axis\" for $rotation_degrees degrees"
	set sel [atomselect $molId $str_selection]
	set old_center [measure center $sel]
	
	# move center to the origin 
	$sel moveby [vecinvert $old_center]

	# rotate 
	set rotation_matrix [transaxis $which_axis $rotation_degrees]
	$sel move $rotation_matrix

	# move back 
	$sel moveby $old_center

	$sel delete
}


proc main {argv} {
	# main function 
	set ccc 0 ;# counter
	set file_psf [lindex $argv $ccc]

	incr ccc
	set file_pdb [lindex $argv $ccc]

	incr ccc
	set file_str_selection [lindex $argv $ccc]

	incr ccc
	set output_prefix [lindex $argv $ccc]

	incr ccc
	set file_rotation_parameters [lindex $argv $ccc]

	set str_selection [get_file_content $file_str_selection]
	set molId [load $file_psf $file_pdb]
	set list_rotation_parameters [get_rotation_parameter_list $file_rotation_parameters]
	puts "roation parameters $list_rotation_parameters"
	foreach parameter_pair $list_rotation_parameters {
		# move
		lassign $parameter_pair which_axis rotation_degrees
		rotate_atoms $molId $str_selection $which_axis $rotation_degrees
	}
	# save
	set str_selection "all"
	write $molId $str_selection $output_prefix
}

#=========================================
main $argv; exit;
#=========================================