# measure RMSD for the whole molecule
# author: Yuhang Wang
# date: 08/03/2015
#=================================================================
proc get_selection_str {in_file_name} {
  ## Read a file and use its content a the returning string 
  set IN [open $in_file_name r]
  set my_str [read $IN]
  close $IN
  return $my_str
}

proc load {file_psf file_ref_pdb file_dcd} {
  ## load psf, pdb and dcd 
  puts "\n\n\n"
  puts "=============================================================="
  puts "--------------------------------------------------------------"
  puts "     Loading $file_psf"
  puts "     Loading $file_ref_pdb"
  puts "     Loading $file_dcd"
  puts "--------------------------------------------------------------"
  set molId_ref    [mol new $file_ref_pdb]
  set molId_target [mol new $file_psf]
 
  mol addfile $file_dcd waitfor all ;# note: molid option doesn't work
  return [list $molId_target $molId_ref]
}

proc align {molId_target molId_ref str_selection_for_align} {
  ## Align every frame to the 1st frame

  puts "--------------------------------------------------------------"
  puts "   Align the trajectory using this selection:"
  puts "   $str_selection_for_align"
  puts "--------------------------------------------------------------"
  set atoms_align_ref     [atomselect $molId_ref $str_selection_for_align]
  set atoms_align_target  [atomselect $molId_target $str_selection_for_align]
  set atoms_to_move     [atomselect $molId_target all]
  set totalNumFrames [molinfo $molId_target get numframes]

  for {set i 0} {$i < $totalNumFrames} {incr i} {
    $atoms_align_target frame $i
    $atoms_to_move frame $i
    $atoms_to_move move [measure fit $atoms_align_target $atoms_align_ref]
  }
  set n1 [$atoms_align_ref num]
  set n2 [$atoms_align_target num]
  $atoms_align_target delete
  $atoms_to_move delete
  $atoms_align_ref delete
  return [list $n1 $n2]

}

proc get_rmsd {molId_target molId_ref str_selection} {
  # measure RMSD frame by frame 
  # relative to frame-0
  puts "--------------------------------------------------------------"
  puts "  Measure RMSD"
  puts "  $str_selection"
  puts "--------------------------------------------------------------"
  
  set list_rmsd {}
  set atoms_rmsd_ref    [atomselect $molId_ref $str_selection]
  set totalNumFrames    [molinfo $molId_target get numframes]
  set atoms_rmsd_target [atomselect $molId_target $str_selection]

  for {set i 1} {$i < $totalNumFrames} {incr i} {
    $atoms_rmsd_target frame $i
    set data_rmsd [measure rmsd $atoms_rmsd_target $atoms_rmsd_ref]
    lappend list_rmsd $data_rmsd
  }
  $atoms_rmsd_target delete
  $atoms_rmsd_ref delete
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

proc main {argv} {
  puts "'------------'"
  set ccc 0
  set file_psf [lindex $argv $ccc]
  puts "in psf  $file_psf"

  incr ccc
  set file_ref_pdb [lindex $argv $ccc]
  puts $file_ref_pdb 

  incr ccc
  set file_dcd [lindex $argv $ccc]

  incr ccc
  set file_output [lindex $argv $ccc]

  incr ccc
  # a file containing an atom selection string for alignment
  set file_selection_for_align [lindex $argv $ccc]

  incr ccc
  # a file containing an atom selection string for the RMSD measurement
  set file_selection_for_rmsd [lindex $argv $ccc]

  ## get atom selection string for alignment
  set str_selection_for_align [get_selection_str $file_selection_for_align]

  ## get atom selection string for RMSD calculation
  set str_selection_for_rmsd [get_selection_str $file_selection_for_rmsd]

  set list_molIds [load $file_psf $file_ref_pdb $file_dcd]
  lassign $list_molIds molId_target molId_ref
  puts "list molIds: $molId_target ; $molId_ref"
  align $molId_target $molId_ref $str_selection_for_align
  set list_rmsd [get_rmsd $molId_target $molId_ref $str_selection_for_rmsd]
  write_output $list_rmsd $file_output
  mol delete $molId_target 
}

#---------------------------------------------------------------------------
#                     MAIN 
#---------------------------------------------------------------------------
main $argv; exit
