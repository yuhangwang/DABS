# Measure center-of-mass distance between two atom selections 
# author: Yuhang Wang
# date: 06/11/2015
#
# note: since Tcl doesn't allow input argument to contain spaces
#     the only way to work around is to use input files that
#     contains an input string (with any number of spaces)
#
# usage: vmd -dispdev text -e get_com_distance.tcl \
#           -args PSF PDB DCD_PREFIX DCD_STAGE_START DCD_STAGE_END OUTPUT_PREFIX \
#                 FILE_SELECTION_1 FILE_SELECTION_2
#
# output: besides the {output_prefix}#.dat files, 
#         another file named {output_prefix}-all.list will also be written
#         which contains a list of names for files generated by this script.
#         This will be very useful for later concatenation.
#
###################################################################################

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
set file_selection_1 [lindex $argv $ccc]

incr ccc
# a file containing an atom selection string for the RMSD measurement
set file_selection_2 [lindex $argv $ccc]

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

proc get_com_distance {molId str_selection_1 str_selection_2} {
  # measure distance between two atom selections 
  puts "--------------------------------------------------------------"
  puts "  Measure distance between two atom selections"
  puts "  (1):  $str_selection_1"
  puts "  (2):  $str_selection_2"
  puts "--------------------------------------------------------------"
  
  set list_distances {}
  set sel1 [atomselect $molId $str_selection_1]
  set sel2 [atomselect $molId $str_selection_2]
  set totalNumFrames [molinfo $molId get numframes]

  for {set i 0} {$i < $totalNumFrames} {incr i} {
    $sel1 frame $i
    $sel2 frame $i
    set coord1 [measure center $sel1 weight mass]
    set coord2 [measure center $sel2 weight mass]
    set distance [veclength [vecsub $coord1 $coord2]]
    lappend list_distances $distance
  }
  $sel1 delete
  $sel2 delete
  return $list_distances
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
set str_selection_1 [get_selection_str $file_selection_1]

## get atom selection string for RMSD calculation
set str_selection_2 [get_selection_str $file_selection_2]

set output_file_list "${output_file_prefix}-all.list"
set OUT [open $output_file_list w]

for {set s $dcd_stage_one} {$s <= $dcd_stage_end} {incr s} {
  set molId [load $in_psf $in_pdb $in_dcd_prefix $s]
  align $molId $str_selection_1
  set list_distances [get_rmsd $molId $str_selection_2]
  set output_file_name "${output_file_prefix}${s}.dat"
  puts $OUT $output_file_name
  write_output $list_distances $output_file_name
  mol delete $molId 
}
close $OUT
exit