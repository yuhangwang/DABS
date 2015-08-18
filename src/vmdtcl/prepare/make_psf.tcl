#=========================================
# Purpose: generate PSF for a given PDB
# Steven(Yuhang) Wang
# 08/09/2012
# updated: 06/09/15
#=========================================
set ccc 0
set pdbName	[lindex $argv $ccc]
incr ccc
set output_dir [lindex $argv $ccc]
incr ccc
set outputNamePrefix	[lindex $argv $ccc]
incr ccc
set list_topology [lindex $argv $ccc]
incr ccc
set patchN [lindex $argv $ccc]
incr ccc
set patchC [lindex $argv $ccc]
incr ccc
set newSegID [lindex $argv $ccc]


#=========================================
# Generate PSF
#=========================================
package require psfgen
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD 

set IN [open $list_topology r]
set all_lines [split [read $IN] "\n"]
close $IN

set ccc 1
set N [llength $all_lines]
foreach topology_file $all_lines {
	topology $topology_file
}

segment $newSegID {
	first $patchN
	last  $patchC
	pdb   $pdbName
}

coordpdb  $pdbName $newSegID

guesscoord  ;# add missing atoms

regenerate angles dihedrals

writepsf ${outputNamePrefix}.psf 
writepdb ${outputNamePrefix}.pdb 

puts "========== DONE! ================="
#==========================================
exit


