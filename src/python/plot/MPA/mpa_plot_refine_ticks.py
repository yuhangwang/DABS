"""
MPA PLOT: REFINE AXIS TICKS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
from mpa_modifier_axis import refine_ticks
#---------------------------------------------------------------

def plot_refine_ticks(object_axis, object_figure, dict_parameters):
	"""
	Refine the figure using parameters stored in the dictionary "dict_parameters"
	:param object object_axis: matplotlib Axis object 
	:param object object_figure: matplotlib Figure object 
	:param dict dict_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = Plot.gca()
	Plot.sca(object_axis)
	#----------------------------------------------------------------------------------------------
	# X and Y Ticks
	#----------------------------------------------------------------------------------------------
	for which_axis in ['x','y']:
		refine_ticks(object_axis, which_axis, 
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
	Plot.sca(object_old_axis_object)
