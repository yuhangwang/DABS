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

def add_grid(object_figure, object_axis, dict_panel_parameters):
	"""
	Add grid to a particular object axis 

	:param object object_figure: matplotlib Figure object 
	:param object object_axis: matplotlib Axis object 
	:param dict dict_panel_parameters: a dictionary of parameters for a particular figure panel 
	"""
	MpaModifierAxis.add_grid(object_figure, object_axis,
		dict_panel_parameters["grid_on"],
		dict_panel_parameters["grid_ticks"],
		dict_panel_parameters["grid_axis"],
		dict_panel_parameters["grid_line_style"],
		dict_panel_parameters["grid_line_width"],
		dict_panel_parameters["grid_line_color"],
		dict_panel_parameters["grid_line_opacity"],
		dict_panel_parameters["grid_z_order"],
		)
	
def refine_ticks(object_axis, dict_panel_parameters):
	"""
	Refine the figure using parameters stored in the dictionary "dict_panel_parameters"
	:param object object_axis: matplotlib Axis object 
	:param dict dict_panel_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = matplotlib.pyplot.gca()
	matplotlib.pyplot.sca(object_axis)
	#----------------------------------------------------------------------------------------------
	# X and Y Ticks
	#----------------------------------------------------------------------------------------------
	for which_axis in ['x','y']:
		MpaModifierAxis.refine_ticks(object_axis, which_axis, 
			tick_major_minor_or_both = dict_panel_parameters[which_axis+"_tick_major_minor_or_both"], 
			tick_in_out_or_inout = dict_panel_parameters[which_axis+"_tick_in_out_or_inout"], 
			tick_length = dict_panel_parameters[which_axis+"_tick_length"], 
			tick_width = dict_panel_parameters[which_axis+"_tick_width"], 
			tick_label_font_size = dict_panel_parameters[which_axis+"_tick_label_font_size"],
			tick_label_font_weight = dict_panel_parameters[which_axis+"_tick_label_font_weight"],
			tick_color = dict_panel_parameters[which_axis+"_tick_color"], 
			tick_label_color = dict_panel_parameters[which_axis+"_tick_label_color"], 
			tick_label_padding = dict_panel_parameters[which_axis+"_tick_label_padding"],
			tick_and_label_z_order = dict_panel_parameters[which_axis+"_tick_and_label_z_order"],
			tick_show_top = dict_panel_parameters[which_axis+"_tick_show_top"],
			tick_show_bottom = dict_panel_parameters[which_axis+"_tick_show_bottom"],
			tick_show_left = dict_panel_parameters[which_axis+"_tick_show_left"],
			tick_show_right = dict_panel_parameters[which_axis+"_tick_show_right"],
			tick_label_show_top = dict_panel_parameters[which_axis+"_tick_label_show_top"],
			tick_label_show_bottom = dict_panel_parameters[which_axis+"_tick_label_show_bottom"],
			tick_label_show_left = dict_panel_parameters[which_axis+"_tick_label_show_left"],
			tick_label_show_right = dict_panel_parameters[which_axis+"_tick_label_show_right"],
			tick_label_number_of_decimal_places = dict_panel_parameters[which_axis+"_tick_label_number_of_decimal_places"],
			tick_reset_old_parameter = dict_panel_parameters[which_axis+"_tick_reset_old_parameter"],
			)
	matplotlib.pyplot.sca(object_old_axis_object)


def hide_tick_label_overlap(object_axis, which_axis, hide_first_how_many, hide_last_how_many, dict_panel_parameters):
	"""
	Hide the overlapping tick labels (either the first or the last tick label)

	:param object object_axis: matplotlib Axis object 
	:param str which_axis: 'x' or 'y'
	:param int hide_first_how_many: a number that decides how many ticks to hide, counting forward
	:param int hide_last_how_many: a number that decides how many ticks to hide, counting backward
	:param dict dict_panel_parameters: a dictionary of parameters for this
		particular figure panel 
	"""
	list_old_tick_labels = MpaModifierAxis.get_tick_labels(object_axis, which_axis)

	if hide_last_how_many == 0: 
		list_new_tick_labels = list_old_tick_labels[hide_first_how_many:]
	else:
		list_new_tick_labels = list_old_tick_labels[hide_first_how_many:-hide_last_how_many]

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
		