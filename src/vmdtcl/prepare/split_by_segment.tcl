#=========================================
# Purpose: split a pdb file by segments
# 	in order to prepare for psfgen
# Steven(Yuhang) Wang
# updated: 06/09/15
#=========================================
set ccc 0
set pdb_name [lindex $argv $ccc]
incr ccc
set input_dir [lindex $argv $ccc]
incr ccc
set output_dir [lindex $argv $ccc]
incr ccc
set output_prefix [lindex $argv $ccc]

set molId [mol new ${input_dir}/$pdb_name]

set all [atomselect $molId all]

set list_segIds [lsort -unique [$all get segname]]

set output_list ${output_dir}/${output_prefix}file_name.list 

set OUT [open $output_list w]

foreach segn $list_segIds {
	puts $segn 
	set tmp_sel [atomselect $molId "segname $segn"]
	set out_name "${output_dir}/${output_prefix}${segn}.pdb"
	puts $OUT $out_name
	$tmp_sel writepdb $out_name
	$tmp_sel delete
}

close $OUT

exit