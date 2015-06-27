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
		

		#----------------------------------------------------------------------------------------------
		# Remove overlapping tick labels
		#----------------------------------------------------------------------------------------------
		if dict_panel_parameters["x_tick_label_hide_overlap"]:
			hide_first_how_many = dict_panel_parameters["x_tick_label_hide_first"]
			hide_last_how_many = dict_panel_parameters["x_tick_label_hide_last"]
			MpaProxyModifierAxis.hide_tick_label_overlap(object_axis, 'x', 
				hide_first_how_many, 
				hide_last_how_many,
				dict_panel_parameters)		
		if dict_panel_parameters["y_tick_label_hide_overlap"]:
			hide_first_how_many = dict_panel_parameters["y_tick_label_hide_first"]
			hide_last_how_many = dict_panel_parameters["y_tick_label_hide_last"]
			MpaProxyModifierAxis.hide_tick_label_overlap(object_axis, 'y', 
				hide_first_how_many, 
				hide_last_how_many,
				dict_panel_parameters)
		
		#----------------------------------------------------------------------------------------------
		# Refine the figure ticks
		#----------------------------------------------------------------------------------------------
		MpaProxyModifierAxis.refine_ticks(object_axis, dict_panel_parameters)


		#----------------------------------------------------------------------------------------------
		# Add grid
		#----------------------------------------------------------------------------------------------
		if dict_panel_parameters["grid_on"]:
			MpaProxyModifierAxis.add_grid(object_figure, object_axis, dict_panel_parameters)