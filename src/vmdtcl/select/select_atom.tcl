#========================================================
# >>>>>>>>>>>>> Select Atoms <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Yuhang Wang
# 07/27/15
# usage: vmd -dispdev text -e select.tcl -args my.psf my.pdb str_selection.txt my_out_prefix
#========================================================

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

	set str_selection [get_file_content $file_str_selection]
	set molId [load $file_psf $file_pdb]
	write $molId $str_selection $output_prefix
}

#=========================================
main $argv; exit;
#=========================================