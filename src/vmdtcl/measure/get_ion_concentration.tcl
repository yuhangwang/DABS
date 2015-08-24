# get ion concentration of a simulation system
# AUTHOR: YUHANG WANG
# DATE: 08/24/2015
# USAGE: vmd -dispdev text -e get_ion_concentration.tcl -args my.pdb 

proc get_selection_str {in_file_name} {
  ## Read a file and use its content a the returning string 
  set IN [open $in_file_name r]
  set my_str [read $IN]
  close $IN
  return $my_str
}

proc load {file_psf} {
  ## load psf
  puts "\n\n\n"
  puts "=============================================================="
  puts "--------------------------------------------------------------"
  puts "     Loading $file_psf"
  puts "--------------------------------------------------------------"
  set molId   [mol new $file_psf]
  return $molId 
}

proc calc_concentration {n_solute n_solvent} {
	# calculate the concentration in mol/L 
	return [expr $n_solute/(($n_solvent*18.)/1000.)]
}

proc get_ion_concentration {molId} {
	set K_ion [atomselect $molId "ions and resname POT"]
	set Na_ion [atomselect $molId "ions and resname SOD"]
	set Cl_ion [atomselect $molId "ions and resname CLA"]
	set All_ions [atomselect $molId "ions"]
	set water_OH2 [atomselect $molId "water and name OH2"]

	set number_K [$K_ion num]
	set number_Na [$Na_ion num]
	set number_Cl [$Cl_ion num]
	set number_ions [$All_ions num]
	set number_water [$water_OH2 num]

	set concentration_K [calc_concentration $number_K $number_water]
	set concentration_Na [calc_concentration $number_Na $number_water]
	set concentration_Cl [calc_concentration $number_Cl $number_water]
	set concentration_ions [calc_concentration $number_ions $number_water]

	return [list $concentration_K $concentration_Na $concentration_Cl $concentration_ions]
}

proc main {argv} {
	puts "'------------'"
	set ccc 0
	set file_psf [lindex $argv $ccc]
	set molId [load $file_psf]
	lassign [get_ion_concentration $molId] concentration_K concentration_Na concentration_Cl concentration_ions
	puts "\[K+\]:  [format %.3f $concentration_K] mol/L"
	puts "\[Na+\]: [format %.3f $concentration_Na] mol/L"
	puts "\[Cl+\]: [format %.3f $concentration_Cl] mol/L"
	puts "\[ion\]: [format %.3f $concentration_ions] mol/L"
}

#---------------------------------------------------------------------------
#                     MAIN 
#---------------------------------------------------------------------------
main $argv; exit

