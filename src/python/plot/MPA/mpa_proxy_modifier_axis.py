"""
MPA PLOT: REFINE AXIS TICKS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
import numpy
import matplotlib.pyplot
#---------------------------------------------------------------
import mpa_modifier_axis   as MpaModifierAxis 
#---------------------------------------------------------------

def refine_ticks_single_axis(object_axis, object_figure, dict_parameters):
	"""
	Refine the figure using parameters stored in the dictionary "dict_parameters"
	:param object object_axis: matplotlib Axis object 
	:param object object_figure: matplotlib Figure object 
	:param dict dict_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = matplotlib.pyplot.gca()
	matplotlib.pyplot.sca(object_axis)
	#----------------------------------------------------------------------------------------------
	# X and Y Ticks
	#----------------------------------------------------------------------------------------------
	for which_axis in ['x','y']:
		MpaModifierAxis.refine_ticks(object_axis, which_axis, 
			tick_major_minor_or_both = dict_parameters[which_axis+"_tick_major_minor_or_both"], 
			tick_in_out_or_inout = dict_parameters[which_axis+"_tick_in_out_or_inout"], 
			tick_length = dict_parameters[which_axis+"_tick_length"], 
			tick_width = dict_parameters[which_axis+"_tick_width"], 
			tick_label_font_size = dict_parameters[which_axis+"_tick_label_font_size"],
			tick_label_font_weight = dict_parameters[which_axis+"_tick_label_font_weight"],
			tick_color = dict_parameters[which_axis+"_tick_color"], 
			tick_label_color = dict_parameters[which_axis+"_tick_label_color"], 
			tick_label_padding = dict_parameters[which_axis+"_tick_label_padding"],
			tick_and_label_z_order = dict_parameters[which_axis+"_tick_and_label_z_order"],
			tick_show_top = dict_parameters[which_axis+"_tick_show_top"],
			tick_show_bottom = dict_parameters[which_axis+"_tick_show_bottom"],
			tick_show_left = dict_parameters[which_axis+"_tick_show_left"],
			tick_show_right = dict_parameters[which_axis+"_tick_show_right"],
			tick_label_show_top = dict_parameters[which_axis+"_tick_label_show_top"],
			tick_label_show_bottom = dict_parameters[which_axis+"_tick_label_show_bottom"],
			tick_label_show_left = dict_parameters[which_axis+"_tick_label_show_left"],
			tick_label_show_right = dict_parameters[which_axis+"_tick_label_show_right"],
			tick_label_number_of_decimal_places = dict_parameters[which_axis+"_tick_label_number_of_decimal_places"],
			tick_reset_old_parameter = dict_parameters[which_axis+"_tick_reset_old_parameter"],
			)
	matplotlib.pyplot.sca(object_old_axis_object)


def refine_ticks_all_axes(list_axis_objects, object_figure, dict_panel_parameters):
	"""
	Refine the ticks for all axes 
	:param list list_axis_objects: list of all axis objects 
	:param object object_figure: matplotlib Figure object 
	:param dict dict_panel_parameters: a dictionary of plot parameters 
	"""
	n_rows, n_columns = numpy.shape(list_axis_objects)
	for i in range(n_rows):
		for j in range(n_columns):
			object_axis = list_axis_objects[i,j]
			refine_ticks_single_axis(object_axis, object_figure, dict_panel_parameters)


def hide_tick_label_overlap(list_axis_objects, dict_panel_parameters):
	"""
	Hide the overlapping tick labels (either the first or the last tick label)
	:param list list_axis_objects: list of axis objects 
	:param dict dict_panel_parameters: a dictionary of plot parameters 
	"""
	if dict_panel_parameters["y_tick_label_hide_overlap"]:
		# remove the first tick label for all but the last row of subplots
		which_axis = 'y'
		for i_row in range(0,dict_panel_parameters['figure_number_of_rows']-1):
			for i_column in range(0,dict_panel_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i_row,i_column]
				list_y_tick_labels = object_axis.get_yticks().tolist()		
				if dict_panel_parameters["y_tick_label_hide_first"]:
					list_new_tick_labels = list_y_tick_labels[1:]
				elif dict_panel_parameters["y_tick_label_hide_last"]:
					list_new_tick_labels = list_y_tick_labels[:-1]
				else:
					list_new_tick_labels = list_y_tick_labels
					MpaModifierAxis.update_ticks_and_labels(object_axis,which_axis, list_new_tick_labels)
		
	if dict_panel_parameters["x_tick_label_hide_overlap"]:
		# remove the first tick label for all but the first column of subplots
		which_axis = 'x'
		for i_row in range(0,dict_panel_parameters['figure_number_of_rows']):
			for i_column in range(1,dict_panel_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i_row,i_column]
				list_x_tick_labels = object_axis.get_xticks().tolist()

				if dict_panel_parameters["x_tick_label_hide_first"]:
					list_new_tick_labels = list_x_tick_labels[1:]
				elif dict_panel_parameters["x_tick_label_hide_last"]:
					list_new_tick_labels = list_x_tick_labels[:-1]
				else:
					list_new_tick_labels = list_x_tick_labels
				MpaModifierAxis.update_ticks_and_labels(object_axis,which_axis, list_new_tick_labels)
	
	return 


def make_panel_axis_limit_tight(object_axis, which_axis, new_min, new_max):
	"""
	Make panel axis limits to match the min/max of the input data series 
	in this particular figure panel.

	:param object object_axis: new axis objects 
	:param str which_axis: 'x' or 'y'
	:param float new_min: new axis minimum 
	:param float new_max: new axis maximum
	"""
	MpaModifierAxis.set_axis_limits(object_axis, which_axis, new_min, new_max)


def set_user_defined_axis_limits(object_axis, dict_panel_parameters):
	"""
	set user-defined axis limits

	:param object object_axis: matplotlib axis object 
	:param float user_x_min: user defined x minimum
	:param float user_x_max: user defined x maximum
	:param float user_y_min: user defined y minimum
	:param float user_y_min: user defined y maximum
	"""
	user_x_min = dict_panel_parameters["x_min"]
	user_x_max = dict_panel_parameters["x_max"]
	user_y_min = dict_panel_parameters["y_min"]
	user_y_max = dict_panel_parameters["y_max"]

	#-------------------------------------------------------------
	# Use user-defined x limits
	#-------------------------------------------------------------
	if dict_panel_parameters["x_limit_user_defined_on"]:
		x_min, x_max = object_axis.get_xlim()
		if user_x_min is not None:
			x_min = user_x_min
			MpaModifierAxis.set_axis_limits(object_axis, 'x', x_min, x_max)
		if user_x_max is not None:
			x_max = user_x_max 
			MpaModifierAxis.set_axis_limits(object_axis, 'x', x_min, x_max)
	
	#-------------------------------------------------------------
	# Use user-defined y limits
	#-------------------------------------------------------------
	if dict_panel_parameters["y_limit_user_defined_on"]:
		y_min, y_max = object_axis.get_ylim()
		if user_y_min is not None:
			y_min = user_y_min
			MpaModifierAxis.set_axis_limits(object_axis, 'y', y_min, y_max)
		if user_y_max is not None:
			y_max = user_y_max 
			MpaModifierAxis.set_axis_limits(object_axis, 'y', y_min, y_max)
		