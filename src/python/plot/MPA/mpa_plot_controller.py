"""
MPA PLOT: LINE 
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#-----------------------------------------------
import mpa_plot_line 	as MpaPlotLine 
import mpa_plot_matrix 	as MpaPlotMatrix 
#-----------------------------------------------
from mpa_data_type_InfoCollector import InfoCollector as MPA_CLASS_InfoCollector
#-----------------------------------------------

def plot(object_figure, 
	list_axis_objects, 
	dict_data_parameters,
	dict_global_parameters,
	):
	"""
	Plot line objects 
	:param object object_figure: a matplotlib Figure object 
	:param list list_axis_objects: list of matplotlib Axis objects 
	:param list dict_data_parameters: a dictionary of user data parameters 
		which file name as key and a dictionary as value
	:param dict dict_global_parameters: a dictionary of global plot parameters 

	"""
	#----------------------------------------------------------------------------------------------
	# Create a PanelDB object to store all newly generated information
	#----------------------------------------------------------------------------------------------
	object_plotObjectInfoCollector = MPA_CLASS_InfoCollector()

	#---------------------------------------------------
	#		Dependency: SciPy
	#---------------------------------------------------
	if dict_global_parameters["use_scipy"] is True:
		import scipy


	#---------------------------------------------------
	# Find the plot type for each data series
	#---------------------------------------------------
	dict_grouped_global_keys = dict()
	for _key in sorted(dict_data_parameters.keys()): # preserve the order of the input data files
		dict_data = dict_data_parameters[_key]
		plot_type = dict_data["data_plot_type"]
		if plot_type not in dict_grouped_global_keys.keys():
			dict_grouped_global_keys[plot_type] = []
		dict_grouped_global_keys[plot_type].append(_key)
	
	#---------------------------------------------------
	# Plot objects 
	#---------------------------------------------------
	[dict_legends, dict_global_xy_minmax, dict_color_bars] = [None, None, None]
	for _plot_type in dict_grouped_global_keys:
		_list_keys = dict_grouped_global_keys[_plot_type]
		if _plot_type == "line":
			[dict_legends, dict_global_xy_minmax] = MpaPlotLine.plot(_list_keys, list_axis_objects, dict_data_parameters, dict_global_parameters)

		if _plot_type == "matrix":
			dict_color_bars = MpaPlotMatrix.plot(_list_keys, list_axis_objects, dict_data_parameters, dict_global_parameters)

	object_plotObjectInfoCollector.set_item("LINE", "dict_legends", dict_legends)
	object_plotObjectInfoCollector.set_item("LINE", "dict_global_xy_minmax", dict_global_xy_minmax)
	object_plotObjectInfoCollector.set_item("MATRIX", "dict_color_bars", dict_color_bars)

	return object_plotObjectInfoCollector.get_dict()