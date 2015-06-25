"""
MPA PLOT: SINGLE AXIS PROPERTIES
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------
import mpa_plot_ticks      as MpaPlotTicks
import mpa_modifier_axis   as MpaModifierAxis 
#---------------------------------------------------

def refine_single_axis(object_axis, object_figure, dict_plot_parameters, 
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
	MpaPlotTicks.set_user_defined_axis_limits(object_axis, dict_plot_parameters,
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


