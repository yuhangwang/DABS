# align an atom selection to its moment of inertia
# AUTHOR: YUHANG WANG
# DATE: 08/17/2015


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


proc recenter {molId str_selection} {
	# recenter the atom selection to the origin
	set sel [atomselect $molId $str_selection]
	set old_center [measure center $sel]
	$sel moveby [vecinvert [measure center $sel]]
	set new_center [measure center $sel]
	puts "old center $old_center"
	puts "new center $new_center"
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
	recenter $molId $str_selection
	set str_selection "all"
	write $molId $str_selection $output_prefix
}

#=========================================
main $argv; exit;
#=========================================