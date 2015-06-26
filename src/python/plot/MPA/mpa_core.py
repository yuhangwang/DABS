"""
MPA: MATPLOTLIB PLOTTING ASSISTANT
AUTHOR: YUHANG WANG
DATE: 06-24-2015
Usage: python mpa.py FILE_LIST-OF-INPUT-DATA-FILE-NAMES FILE_PLOT-PARAMETERS
"""
#================================================
# Use Python 3 compatibility
#================================================
from __future__ import print_function, division
#================================================
import matplotlib
import matplotlib.pyplot 
import sys
import re
import numpy 
import pyparsing
#------------------------------------------------
# MPA Internal modules
#------------------------------------------------
import mpa_core_io   as MPA_IO
import mpa_core_plot as MPA_PLOT
from mpa_core_parameter import GlobalParameters    as MPA_CLASS_GlobalParameters
from mpa_core_parameter import LocalParameters     as MPA_CLASS_LocalParameters
from mpa_core_parameter import InputFileParameters as MPA_CLASS_InputFileParameters
#================================================

def main(file_input_information, file_plot_parameters, preview=False):
	"""
	Main entry for MPA 
	:param str file_input_information: file name for all input file information 
	:param str file_plot_parameters: file name for plotting parameter file 
	:param bool preview: True | False(default) which decide whether to show a
		preview of the figure 
	"""
	#-------------------------------------------------------------------
	# [1] Read inputs
	#-------------------------------------------------------------------
	dict_default_input_parameters = MPA_CLASS_InputFileParameters.get_defaults()
	dict_convention_input_parameters = MPA_CLASS_InputFileParameters.get_convention()
	list_input_information = MPA_IO.read_input(file_input_information, 
		dict_default_input_parameters,
		dict_convention_input_parameters)
	
	object_parameter_global = MPA_CLASS_GlobalParameters()
	object_parameter_local = MPA_CLASS_LocalParameters()
	dict_plot_parameters = MPA_IO.read_parameter(file_plot_parameters,
						object_parameter_global,
						object_parameter_local)

	#-------------------------------------------------------------------
	# [3] Plot
	#-------------------------------------------------------------------
	object_figure, list_axis_objects = MPA_PLOT.plot(list_input_information, dict_plot_parameters)

	#-----------------------------------------------------------------
	# [4] Save
	#-----------------------------------------------------------------
	MPA_IO.write_figure(object_figure, 
		dict_plot_parameters["figure_output_file_name"],
		figure_dpi = dict_plot_parameters["figure_dpi"],
		figure_padding = dict_plot_parameters["figure_padding"],
		figure_transparent = dict_plot_parameters["figure_transparent"],
		)
	
	#-----------------------------------------------------------------
	# [5] Preview?
	#-----------------------------------------------------------------
	if preview: matplotlib.pyplot.show()

	return (object_figure, list_axis_objects)


if __name__ == '__main__':
	ccc = 1
	file_input_information = sys.argv[ccc]
	ccc += 1
	file_plot_parameters = sys.argv[ccc]

	preview=True
	main(file_input_information, file_plot_parameters, preview)

	