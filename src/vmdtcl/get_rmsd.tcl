# Measure RMSD for the whole molecule
# author: Yuhang Wang
# date: 06/11/2015
# note: since Tcl doesn't allow input argument to contain spaces
#     the only way to work around is to use input files that
#     contains an input string (with any number of spaces)
# usage: vmd -dispdev text -e get_rmsd.tcl \
#           -args PSF PDB DCD_PREFIX DCD_STAGE_START DCD_STAGE_END OUTPUT_PREFIX \
#                 FILE_SELECTION_FOR_ALIGN FILE_SELECTION_FOR_RMSD

puts "'------------'"
set ccc 0
set in_psf [lindex $argv $ccc]
puts "in psf  $in_psf"
incr ccc
set in_pdb [lindex $argv $ccc]
puts $in_pdb 

incr ccc
set in_dcd_prefix [lindex $argv $ccc]

incr ccc
set dcd_stage_one [lindex $argv $ccc]

incr ccc
set dcd_stage_end [lindex $argv $ccc]

incr ccc
set output_file_prefix [lindex $argv $ccc]

incr ccc
# a file containing an atom selection string for alignment
set file_selection_for_align [lindex $argv $ccc]

incr ccc
# a file containing an atom selection string for the RMSD measurement
set file_selection_for_rmsd [lindex $argv $ccc]

#=================================================================
proc get_selection_str {in_file_name} {
  ## Read a file and use its content a the returning string 
  set IN [open $in_file_name r]
  set my_str [read $IN]
  close $IN
  return $my_str
}
proc load {in_psf in_pdb in_dcd_prefix stage} {
  ## load psf, pdb and dcd for stage i
  set file_dcd "${in_dcd_prefix}${stage}.dcd"
  puts "\n\n\n"
  puts "=============================================================="
  puts "--------------------------------------------------------------"
  puts "     Loading $in_psf"
  puts "     Loading $in_pdb"
  puts "     Loading $file_dcd"
  puts "--------------------------------------------------------------"
  set molId [mol new $in_psf]
  mol addfile $in_pdb molid $molId 
 
  mol addfile $file_dcd waitfor all molid $molId 
  return $molId
}

proc align {molId str_selection_for_align} {
  ## Align every frame to the 1st frame

  puts "--------------------------------------------------------------"
  puts "   Align the trajectory using this selection:"
  puts "   $str_selection_for_align"
  puts "--------------------------------------------------------------"
  set ref [atomselect $molId $str_selection_for_align frame 0]
  set totalNumFrames [molinfo $molId get numframes]

  for {set i 1} {$i < $totalNumFrames} {incr i} {
    set sel [atomselect $molId $str_selection_for_align frame $i]
    set frame_i [atomselect $molId all frame $i]
    $frame_i move [measure fit $sel $ref]
    $sel delete
    $frame_i delete
  }
  $ref delete
}

proc get_rmsd {molId str_selection} {
  # measure RMSD frame by frame 
  # relative to frame-0
  puts "--------------------------------------------------------------"
  puts "  Measure RMSD"
  puts "  $str_selection"
  puts "--------------------------------------------------------------"
  
  set list_rmsd {}
  set ref [atomselect $molId $str_selection frame 0]
  set totalNumFrames [molinfo $molId get numframes]

  for {set i 1} {$i < $totalNumFrames} {incr i} {
    set sel [atomselect $molId $str_selection frame $i]
    set data_rmsd [measure rmsd $sel $ref]
    lappend list_rmsd $data_rmsd
    $sel delete
  }
  $ref delete
  return $list_rmsd
}

proc write_output {in_list output_file_name} {
  puts "--------------------------------------------------------------"
  puts "  Output file: "
  puts "  $output_file_name"
  puts "--------------------------------------------------------------"
  set OUT [open $output_file_name w]
  foreach data $in_list {
      puts $OUT $data
  }
  close $OUT
}

#---------------------------------------------------------------------------
#                     MAIN 
#---------------------------------------------------------------------------

## get atom selection string for alignment
set str_selection_for_align [get_selection_str $file_selection_for_align]

## get atom selection string for RMSD calculation
set str_selection_for_rmsd [get_selection_str $file_selection_for_rmsd]

set output_file_list "${output_file_prefix}-all.list"
set OUT [open $output_file_list w]

for {set s $dcd_stage_one} {$s <= $dcd_stage_end} {incr s} {
  set molId [load $in_psf $in_pdb $in_dcd_prefix $s]
  align $molId $str_selection_for_align
  set list_rmsd [get_rmsd $molId $str_selection_for_rmsd]
  set output_file_name "${output_file_prefix}${s}.dat"
  puts $OUT $output_file_name
  write_output $list_rmsd $output_file_name
  mol delete $molId 
}
close $OUT
exit
