"""
MPA PLOT: SINGLE AXIS PROPERTIES
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------
import mpa_modifier_axis   		 as MpaModifierAxis 
import mpa_proxy_modifier_axis   as MpaProxyModifierAxis
#---------------------------------------------------

def refine_figure_panel(object_axis, object_figure, dict_plot_parameters, 
	user_x_min,
	user_x_max,
	user_y_min,
	user_y_max,
	):
	"""
	Refine each axis 
	:param object object_axis: a matplotlib Axis object 
	:param object object_figure: a matplotlib Figure object 
	:param dict dict_plot_parameters: a dictionary of plotting parameters 
	:param float: user_x_min: user-defined minimum for x axis 
	:param float: user_x_max: user-defined maximum for x axis 
	:param float: user_y_min: user-defined minimum for y axis 
	:param float: user_y_max: user-defined maximum for y axis 
	"""

	#-------------------------------------------------------------
	# set user defined axis limits
	#-------------------------------------------------------------
	MpaProxyModifierAxis.set_user_defined_axis_limits(object_axis, dict_plot_parameters,
		user_x_min,
		user_x_max,
		user_y_min,
		user_y_max,
		)

	#---------------------------------------------------------------
	# Grid
	#---------------------------------------------------------------
	MpaModifierAxis.add_grid(object_figure, 
		dict_plot_parameters["show_grid"],
		dict_plot_parameters["grid_ticks"],
		dict_plot_parameters["grid_axis"],		
		dict_plot_parameters["grid_line_style"],
		dict_plot_parameters["grid_line_width"],
		dict_plot_parameters["grid_line_color"],
		dict_plot_parameters["grid_line_opacity"],
		dict_plot_parameters["grid_z_order"])


def refine_all_figure_panels(object_figure, list_axis_objects, dict_legends,
	dict_local_parameters):
	"""
	Refine the 
	:param object objec_figure: maplotlib Figure object 
	:param list list_axis_objects: list of matplotlib Axis objects 
	:param dict dict_local_parameters: a python dict of local plot parameters with panel indices as keys
		and sub-dictionaries as values
	:param dict dict_legends: a python dict of legend parameters for all axes 
		with panel indices as keys and sub-dictionaries as values 
	"""

	for panel_indices, dict_plot_parameters in dict_local_parameters.items():
		i_row, i_column = panel_indices
		object_axis = list_axis_objects[i_row, i_column]

		# Refine axis limits
		MpaProxyModifierAxis.set_user_defined_axis_limits(object_axis, dict_plot_parameters)


	