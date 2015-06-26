"""
MPA PLOT
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
import matplotlib.pyplot
import numpy
#---------------------------------------------------------------
import mpa_plot_property_all_axes as MpaPlotProertyAllAxes 
import mpa_plot_line              as MpaPlotLine 
import mpa_plot_create			  as MpaPlotCreate 
#---------------------------------------------------------------


def plot(dict_file_parameters, dict_global_parameters, dict_local_parameters):
	"""
	Plot every data series in dict_file_parameters
	
	:param list dict_file_parameters: a list of dictionaries
	:param dict dict_global_parameters: a python dictionary of global plotting parameters
	:param dict dict_local_parameters: a python dictionary of local plotting parameters (per figure panel)
	:return: object for the current plot
	"""
	#-------------------------------------------------------------------
	# Manage external dependencies
	#-------------------------------------------------------------------
	#---------------------------------------------------
	#		Dependency: Latex
	#---------------------------------------------------
	if dict_global_parameters["use_latex"] is True:
		matplotlib.rcParams['text.usetex'] = True
		matplotlib.rcParams['text.latex.unicode'] = True
		matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']

	#-------------------------------------------------------------------
	# Create a list of figure/axis objects 
	#-------------------------------------------------------------------
	[object_figure, list_axis_objects, dict_global_parameters] = MpaPlotCreate.figure(dict_global_parameters)
	
	#-------------------------------------------------------------------
	# Plot lines
	#-------------------------------------------------------------------
	[array2D_global_x_min, array2D_global_x_max, 
	 array2D_global_y_min, array2D_global_y_max,
	 dict_panel_information] = MpaPlotLine.plot(object_figure, 
					 							list_axis_objects,
					 							dict_local_parameters,
												dict_file_parameters)
	
	#----------------------------------------------------------------------------------------------
	# Refine properties for all axes
	#----------------------------------------------------------------------------------------------
	MpaPlotProertyAllAxes.refine_all_axes(object_figure, list_axis_objects, dict_global_parameters, dict_panel_information,
		array2D_global_x_min,
		array2D_global_x_max,
		array2D_global_y_min,
		array2D_global_y_max,
		)

	return (object_figure, list_axis_objects)
