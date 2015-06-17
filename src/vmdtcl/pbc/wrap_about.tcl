# Wrap certain atoms about the center of another atom selection
# Author: Yuhang Wang
# Date: 06/17/2015
# Usage: vmd -dispdev text -e PSF_FILE DCD_FILE OUTPUT_FILE \
#       FILE_STRING_SELECTION_TO_WRAP \
#       FILE_STRING_SELECTION_TO_CENTER
#

package require pbctools

set ccc 0
set in_psf [lindex $argv $ccc]

incr ccc
set in_dcd [lindex $argv $ccc]

incr ccc
set output_file_name [lindex $argv $ccc]

incr ccc
set file_str_selection_to_wrap [lindex $argv $ccc]

incr ccc
set file_str_selection_center [lindex $argv $ccc]

#=================================================================
proc get_selection_str {in_file_name} {
  ## Read a file and use its content a the returning string 
  set IN [open $in_file_name r]
  set my_str [read $IN]
  close $IN
  return $my_str
}

proc load {in_psf in_dcd} {
  ## load psf, and dcd 
  puts "=============================================================="
  puts "--------------------------------------------------------------"
  puts "     Loading $in_psf"
  puts "     Loading $in_dcd"
  puts "--------------------------------------------------------------"
  set molId [mol new $in_psf]
 
  mol addfile $in_dcd waitfor all molid $molId 
  return $molId
}

proc wrap {molId str_selection_to_wrap str_selection_center} {
  pbc wrap -center com -centersel $str_selection_center -compound res -sel  $str_selection_to_wrap -first first -last last -molid $molId
}

proc write_output {molId output_file_name} {
  animate write dcd $output_file_name waitfor all $molId
}

#---------------------------------------------------------------------------
#                     MAIN 
#---------------------------------------------------------------------------

## string for selecting atoms to be wrapped
set str_selection_to_wrap [get_selection_str $file_str_selection_to_wrap]

## string for selecting atoms to be the center
set str_selection_center [get_selection_str $file_str_selection_center]

## Load
set molId [load $in_psf $in_dcd]

## Wrap
wrap $molId $str_selection_to_wrap $str_selection_center

# ## Output
write_output $molId $output_file_name

## Clean up
mol delete $molId 

puts "============================================================="
puts "                         DONE!                               "
puts "  Output: $output_file_name                                  "
puts "============================================================="
exit

exit
