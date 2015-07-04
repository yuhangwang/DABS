"""
MPA PLOT: MATRIX
AUTHOR: YUHANG WANG
DATE: 07-03-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
import numpy
import matplotlib.pyplot 
#-----------------------------------------------
from mpa_data_type_InfoCollector import InfoCollector as MPA_CLASS_InfoCollector
#---------------------------------------------------------------

def plot(list_data_keys, list_axis_objects, dict_data_parameters, dict_global_parameters):
	"""
	Plot line objects; optionally plot the block-average
	:param list list_data_keys: dictionary keys for items to be plotted in dict_data_parameters
	:param list list_axis_objects: list of matplotlib Axis objects 
	:param dict dict_data_parameters: a dictionary of user data parameters 
	:param dict dict_global_parameters: a dictionary of global plot parameters
	:return: (dict_legends, dict_global_xy_minmax) 
	Example usage: 
		object_axis = dict_legends[(0,1)]["objec_axis"]
		data_x_min = dict_global_xy_minmax[(0,0)]['x']["min"]
	"""
	#----------------------------------------------------------------------------------------------
	# Create a PanelDB object to store all panel information
	#----------------------------------------------------------------------------------------------
	object_colorBarInfoCollector = MPA_CLASS_InfoCollector()

	#----------------------------------------------------------------------------------------------
	# ========= *** Start Plotting!  *** ================
	#----------------------------------------------------------------------------------------------
	for _key in list_data_keys: 
		dict_data = dict_data_parameters[_key]
		tuple_panel_indices = dict_data["data_panel_indices"]
		panel_id_row, _panel_id_column = tuple_panel_indices
		object_axis_for_panel = list_axis_objects[panel_id_row, _panel_id_column]

		#-------------------------------------------------
		# User data
		#-------------------------------------------------
		user_data = dict_data["data_value"]
		if dict_data["data_matrix_transpose"]:
			user_data = numpy.transpose(user_data)

		# skip dummy axis objects
		#-------------------------------------------------
		if object_axis_for_panel is None: 
			print("skip", tuple_panel_indices)
			continue

		#-------------------------------------------------
		# Set the current active Axes instance to this axis 
		#-------------------------------------------------
		matplotlib.pyplot.sca(object_axis_for_panel)

		#-------------------------------------------------
		#  Plot!
		#-------------------------------------------------
		print("panel: ", tuple_panel_indices)
		object_matrix_plot = object_axis_for_panel.matshow(user_data)

		#-------------------------------------------------
		# Collect color bar information
		#-------------------------------------------------
		if dict_data["data_matrix_color_bar_on"]:
			tuple_color_bar_panel_indices = dict_data["data_matrix_color_bar_panel_indices"] # note: this can be different than tuple_panel_indices
			id_row_legend_panel, id_column_legend_panel = tuple_color_bar_panel_indices
			object_axis_for_color_bar = list_axis_objects[id_row_legend_panel, id_column_legend_panel]

			# axis object
			object_colorBarInfoCollector.set_item(tuple_color_bar_panel_indices, 
				"object_axis", object_axis_for_color_bar)

			# add object_matrix_plot
			object_colorBarInfoCollector.set_item(tuple_color_bar_panel_indices,
				"object_matrix_plot", object_matrix_plot)
			

		dict_color_bars = object_colorBarInfoCollector.get_dict()

	return dict_color_bars