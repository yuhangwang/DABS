# Merge many molecules into one system 
# Author: Yuhang Wang
# Date: 07/29/2015
# Usage: vmd -dispdev text -e merge_molecules.tcl -args psf_pdb.list output_prefix

package require topotools 

proc get_list_of_psf_pdb {file_name} {
	# Read a file
	# Return its content as one string 
	set IN [open $file_name r]
	set list_lines [split [read $IN] '\n'] 
	close $IN

	set list_output {}
	foreach line $list_lines {
		if { $line == ""} {continue}
		lassign [split $line] file_psf file_pdb 
		lappend list_output [list $file_psf $file_pdb]
	}
	return $list_output
}

proc load {file_psf file_pdb} {
	# load a pair of psf/pdb files 
	# return the VMD molecule ID 
	set molId [mol new $file_psf]
	mol addfile $file_pdb
	return $molId 
}


proc merge {list_molIds output_prefix} {
	# Merge many molecules 
	set molId [::TopoTools::mergemols $list_molIds]
	animate write psf ${output_prefix}.psf $molId 
	animate write pdb ${output_prefix}.pdb $molId
}


proc main {argv} {
	set ccc 0
	set file_list_of_psf_pdb [lindex $argv $ccc]

	incr ccc
	set output_prefix [lindex $argv $ccc]

	set list_psf_pdb [get_list_of_psf_pdb $file_list_of_psf_pdb]
	
	set list_molIds {}
	foreach file_pair $list_psf_pdb {
		lassign $file_pair file_psf file_pdb 
		set molId [load $file_psf $file_pdb]
		lappend list_molIds $molId
	}

	merge $list_molIds $output_prefix

}

#=========================================
main $argv; exit;
#=========================================