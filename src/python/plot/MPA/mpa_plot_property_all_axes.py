"""
MPA PLOT: ALL AXIS PROPERTIES
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------
import matplotlib.pyplot
#---------------------------------------------------
import mpa_proxy_modifier_axis        as MpaProxyModifierAxis 
import mpa_modifier_axis              as MpaModifierAxis 
import mpa_proxy_modifier_legend      as MpaProxyModifierLegend  
import mpa_proxy_modifier_panel_label as MpaProxyModifierPanelLabel 
#---------------------------------------------------

def add_axis_labels(object_figure, dict_plot_parameters):
	"""
	Add the common X/Y axis labels and figure title 
	"""
	#----------------------------------------------------------
	# make an extra axis just to show the common X/Y label
	#----------------------------------------------------------
	object_extra_axis = object_figure.add_subplot(1,1,1)
	object_extra_axis.patch.set_alpha(0.)

	# turn off the extra axis's tick labels
	matplotlib.pyplot.setp(object_extra_axis.get_xticklabels(), visible=False)
	matplotlib.pyplot.setp(object_extra_axis.get_yticklabels(), visible=False)
	object_extra_axis.set_xticks([])
	object_extra_axis.set_yticks([])

	# Make the frame line transparent
	for child in object_extra_axis.get_children():
		if isinstance(child, matplotlib.spines.Spine):
			child.set_color((0,0,0,0))

	# Figure title
	if dict_plot_parameters["figure_title"] is not None:
		MpaModifierFigure .add_title(object_extra_axis, dict_plot_parameters["figure_title"], dict_plot_parameters["figure_title_font_size"])

	#----------------------------------------------------------------------------------------------
	#	Axis Label
	#----------------------------------------------------------------------------------------------
	MpaModifierAxis.add_axis_label(object_extra_axis, 'x', dict_plot_parameters["x_label"], dict_plot_parameters["x_label_font_size"],
		dict_plot_parameters["x_label_padding"])
	MpaModifierAxis.add_axis_label(object_extra_axis, 'y', dict_plot_parameters["y_label"], dict_plot_parameters["y_label_font_size"],
		dict_plot_parameters["y_label_padding"])
	


def refine_all_axes(object_figure, list_axis_objects, dict_plot_parameters, dict_panel_information,
	array2D_global_x_min,
	array2D_global_x_max,
	array2D_global_y_min,
	array2D_global_y_max,
	):
	"""
	Refine properties for all axes 
	:param list list_axis_objects: list of axis objects 
	:param dict dict_plot_parameters: plot parameter dictionary
	:param dict dict_panel_information: figure panel information dictionary
	:param list array2D_global_x_min: a 2D list of global x minimum for every axis 
	:param list array2D_global_x_max: a 2D list of global x maximum for every axis 
	:param list array2D_global_y_min: a 2D list of global y minimum for every axis 
	:param list array2D_global_y_max: a 2D list of global y maximum for every axis 
	"""

	#----------------------------------------------------------------------------------------------
	# Add axis labels
	#----------------------------------------------------------------------------------------------
	add_axis_labels(object_figure, dict_plot_parameters)

	#----------------------------------------------------------------------------------------------
	# Add figure panel label
	#----------------------------------------------------------------------------------------------
	MpaProxyModifierPanelLabel.add_figure_panel_labels(dict_panel_information, dict_plot_parameters)

	#----------------------------------------------------------------------------------------------
	# Add & refine legend
	#----------------------------------------------------------------------------------------------
	MpaProxyModifierLegend.refine_legend(dict_panel_information, dict_plot_parameters)

	#----------------------------------------------------------------------------------------------
	# Make axis limits tight
	#----------------------------------------------------------------------------------------------
	MpaProxyModifierAxis.make_all_axis_limits_tight(list_axis_objects, dict_plot_parameters,
		array2D_global_x_min,
		array2D_global_x_max,
		array2D_global_y_min,
		array2D_global_y_max,
		)

	#----------------------------------------------------------------------------------------------
	# Remove overlapping tick labels
	#----------------------------------------------------------------------------------------------
	MpaProxyModifierAxis.hide_tick_label_overlap(list_axis_objects, dict_plot_parameters)
	
	#----------------------------------------------------------------------------------------------
	# Refine the figure ticks
	#----------------------------------------------------------------------------------------------
	MpaProxyModifierAxis.refine_ticks_all_axes(list_axis_objects, object_figure, dict_plot_parameters)
