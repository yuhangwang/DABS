"""
MPA PLOT: SINGLE AXIS PROPERTIES
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------
import mpa_proxy_modifier_axis        as MpaProxyModifierAxis 
import mpa_proxy_modifier_panel 	  as MpaProxyModifierPanel 
import mpa_proxy_modifier_legend      as MpaProxyModifierLegend  
#---------------------------------------------------

def refine_figure_panel(object_axis, object_figure, dict_panel_parameters, 
	user_x_min,
	user_x_max,
	user_y_min,
	user_y_max,
	):
	"""
	Refine each axis 
	:param object object_axis: a matplotlib Axis object 
	:param object object_figure: a matplotlib Figure object 
	:param dict dict_panel_parameters: a dictionary of plotting parameters 
	:param float: user_x_min: user-defined minimum for x axis 
	:param float: user_x_max: user-defined maximum for x axis 
	:param float: user_y_min: user-defined minimum for y axis 
	:param float: user_y_max: user-defined maximum for y axis 
	"""

	#-------------------------------------------------------------
	# set user defined axis limits
	#-------------------------------------------------------------
	MpaProxyModifierAxis.set_user_defined_axis_limits(object_axis, dict_panel_parameters,
		user_x_min,
		user_x_max,
		user_y_min,
		user_y_max,
		)

	#---------------------------------------------------------------
	# Grid
	#---------------------------------------------------------------
	MpaModifierAxis.add_grid(object_figure, 
		dict_panel_parameters["show_grid"],
		dict_panel_parameters["grid_ticks"],
		dict_panel_parameters["grid_axis"],		
		dict_panel_parameters["grid_line_style"],
		dict_panel_parameters["grid_line_width"],
		dict_panel_parameters["grid_line_color"],
		dict_panel_parameters["grid_line_opacity"],
		dict_panel_parameters["grid_z_order"])


def refine_all_figure_panels(object_figure, list_axis_objects, 
	dict_legends,
	dict_global_xy_minmax,
	dict_local_parameters):
	"""
	Refine the 
	:param object objec_figure: maplotlib Figure object 
	:param list list_axis_objects: list of matplotlib Axis objects 
	:param dict dict_legends: a python dict of legend parameters for all axes 
		with panel indices as keys and sub-dictionaries as values 
	:param dict dict_global_xy_minmax: a dictionary of global x/y min/max for each figure panel 
	:param dict dict_local_parameters: a python dict of local plot parameters with panel indices as keys
		and sub-dictionaries as values
	"""

	for panel_indices, dict_panel_parameters in dict_local_parameters.items():
		i_row, i_column = panel_indices
		object_axis = list_axis_objects[i_row, i_column]

		# Control: legend
		if panel_indices in dict_legends.keys():
			isPanelLegendOn = dict_legends[panel_indices]["panel_legend_on"]
			dict_legend_of_current_panel = dict_legends[panel_indices]
		else:
			isPanelLegendOn = False


		#----------------------------------------------------------------------------------------------
		# Refine axis limits
		#----------------------------------------------------------------------------------------------
		MpaProxyModifierAxis.set_user_defined_axis_limits(object_axis, dict_panel_parameters)

		#----------------------------------------------------------------------------------------------
		# Add figure panel label
		#----------------------------------------------------------------------------------------------
		MpaProxyModifierPanel.add_figure_panel_labels(object_axis, dict_panel_parameters)

		#----------------------------------------------------------------------------------------------
		# Add & refine legend
		#----------------------------------------------------------------------------------------------
		if isPanelLegendOn:
			MpaProxyModifierLegend.refine_legend(dict_legend_of_current_panel, dict_panel_parameters)

		#----------------------------------------------------------------------------------------------
		# Make axis limits tight
		#----------------------------------------------------------------------------------------------
		if dict_panel_parameters["x_limit_tight_on"]:
			new_min = dict_global_xy_minmax[panel_indices]['x']['min']
			new_max = dict_global_xy_minmax[panel_indices]['x']['max']
			print("New X min: {0}  max: {1}".format(new_min, new_max))
			MpaProxyModifierAxis.make_panel_axis_limit_tight(object_axis, 'x', new_min, new_max)

		if dict_panel_parameters["y_limit_tight_on"]:
			new_min = dict_global_xy_minmax[panel_indices]['y']['min']
			new_max = dict_global_xy_minmax[panel_indices]['y']['max']
			print("New Y min: {0}  max: {1}".format(new_min, new_max))
			MpaProxyModifierAxis.make_panel_axis_limit_tight(object_axis, 'y', new_min, new_max)
		

		# #----------------------------------------------------------------------------------------------
		# # Remove overlapping tick labels
		# #----------------------------------------------------------------------------------------------
		# MpaProxyModifierAxis.hide_tick_label_overlap(list_axis_objects, dict_panel_parameters)
		
		# #----------------------------------------------------------------------------------------------
		# # Refine the figure ticks
		# #----------------------------------------------------------------------------------------------
		# MpaProxyModifierAxis.refine_ticks_all_axes(list_axis_objects, object_figure, dict_panel_parameters)

