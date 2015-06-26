"""
MPA PLOT: LINE 
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#-----------------------------------------------
import numpy
import matplotlib.pyplot 
#-----------------------------------------------
from mpa_data_type_PanelDB import PanelDB as MPA_CLASS_PanelDB
import mpa_toolkit                   as MpaTool 
import mpa_plot_property_single_axis as MpaPlotPropertySingleAxis 
#-----------------------------------------------

def plot(object_figure, 
	list_axis_objects, 
	dict_plot_parameters,
	list_input_information,
	):
	"""
	Plot line objects 
	:param object object_figure: a matplotlib Figure object 
	:param list list_axis_objects: list of matplotlib Axis objects 
	:param dict dict_plot_parameters: a dictionary of MPA plot parameters 
	:param list list_input_information: a list of dictionaries of input information for each axis 
	:return: (array2D_global_x_min, array2D_global_x_max, 
			  array2D_global_y_min, array2D_global_y_max,
			  dict_panel_information)
	"""
	#---------------------------------------------------
	#		Dependency: SciPy
	#---------------------------------------------------
	if dict_plot_parameters["use_scipy"] is True:
		import scipy
		if dict_plot_parameters["show_block_averaged_line"] is False:
			msg = "ERROR HINT: you must set \"USE SCIPY\" = True to use \"SHOW BLOCK AVERAGED LINE\" \n"
			raise UserWarning(msg)

	#----------------------------------------------------------------------------------------------
	# make a 2D array to store the global min/max for each figure axis
	#----------------------------------------------------------------------------------------------
	n_rows = dict_plot_parameters["figure_number_of_rows"]
	n_columns = dict_plot_parameters["figure_number_of_columns"]
	array2D_global_x_min = MpaTool.initialize_a_2d_array_with_None(n_rows, n_columns)
	array2D_global_x_max = MpaTool.initialize_a_2d_array_with_None(n_rows, n_columns)
	array2D_global_y_min = MpaTool.initialize_a_2d_array_with_None(n_rows, n_columns)
	array2D_global_y_max = MpaTool.initialize_a_2d_array_with_None(n_rows, n_columns)

	#----------------------------------------------------------------------------------------------
	# Create a PanelDB object to store all panel information
	#----------------------------------------------------------------------------------------------
	object_panelDB = MPA_CLASS_PanelDB()

	#----------------------------------------------------------------------------------------------
	# ========= *** Start Plotting!  *** ================
	#----------------------------------------------------------------------------------------------
	ccc = 0
	for dict_user_input in list_input_information:
		tuple_panel_indices = dict_user_input["panel_indices"]
		user_data   = dict_user_input["input_data"]
		panel_id_row, panel_id_column = tuple_panel_indices
		object_axis_for_panel = list_axis_objects[panel_id_row, panel_id_column]


		# skip dummy axis objects
		if object_axis_for_panel is None: 
			print("skip", tuple_panel_indices)
			continue

		# Get X & Y from user_data
		X = user_data[:,0]
		Y = user_data[:,1]


		# set line color
		list_colors = dict_plot_parameters["color_order"]
		line_color = list_colors[ccc%len(list_colors)]


		# User-defined axis min/max 
		user_x_min = dict_user_input["x_min"]
		user_x_max = dict_user_input["x_max"]
		user_y_min = dict_user_input["y_min"]
		user_y_max = dict_user_input["y_max"]
		# update global min/max along X
		x_min = numpy.amin(X)
		x_max = numpy.amax(X)
		y_min = numpy.amin(Y)
		y_max = numpy.amax(Y)
		array2D_global_x_min[panel_id_row][panel_id_column] = MpaTool.return_smaller(array2D_global_x_min[panel_id_row][panel_id_column], x_min)
		array2D_global_x_max[panel_id_row][panel_id_column] = MpaTool.return_bigger(array2D_global_x_max[panel_id_row][panel_id_column], x_max)
		array2D_global_y_min[panel_id_row][panel_id_column] = MpaTool.return_smaller(array2D_global_y_min[panel_id_row][panel_id_column], y_min)
		array2D_global_y_max[panel_id_row][panel_id_column] = MpaTool.return_bigger(array2D_global_y_max[panel_id_row][panel_id_column], y_max)


		# Set the current active Axes instance to this axis 
		matplotlib.pyplot.sca(object_axis_for_panel)

		#-------------------------------------------------
		#  Plot!
		#-------------------------------------------------
		object_line, = object_axis_for_panel.plot(X,Y, 
			color=line_color,
			alpha=dict_plot_parameters["line_opacity"],
			linestyle=dict_plot_parameters["line_style"],
			)

		#-------------------------------------------------------------
		# Also plot the noise-filtered-averaged line
		#-------------------------------------------------------------
		if dict_plot_parameters["show_block_averaged_line"]:
			from scipy import ndimage
			Y_block_averaged = ndimage.filters.uniform_filter(Y, 
				size=dict_user_input["line_block_average_block_size"], 
				mode="nearest")
			object_line, = object_axis_for_panel.plot(X,Y_block_averaged,
				linewidth=dict_plot_parameters["block_averaged_line_width"],
				color=line_color,
				)

		#-------------------------------------------------------------
		# Add panel label information
		#-------------------------------------------------------------
		# panel label
		object_panelDB.set_item(tuple_panel_indices,
			"panel_label", dict_user_input["panel_label"])
		
		# panel label coordinate
		object_panelDB.set_item(tuple_panel_indices,
			"panel_label_coordinate", dict_user_input["panel_label_coordinate"])
		
		# panel axis object
		object_panelDB.set_item(tuple_panel_indices,
			"object_axis", object_axis_for_panel)

		#-------------------------------------------------------------
		# Add panel legend information
		#-------------------------------------------------------------
		tuple_legend_panel_indices = dict_user_input["legend_panel_indices"]
		id_row_legend_panel, id_column_legend_panel = tuple_legend_panel_indices
		object_axis_for_legend = list_axis_objects[id_row_legend_panel, id_column_legend_panel]
		
		# active legend for this axis
		object_panelDB.set_item(tuple_legend_panel_indices,
			"legend_on", True)

		# axis object
		object_panelDB.set_item(tuple_legend_panel_indices, 
			"object_axis", object_axis_for_legend)

		# legend anchor coordinate
		object_panelDB.set_item(tuple_legend_panel_indices, 
			"legend_anchor_coordinate", dict_user_input["legend_anchor_coordinate"])

		# legend number of columns
		object_panelDB.set_item(tuple_legend_panel_indices,
			"legend_number_of_columns", dict_user_input["legend_number_of_columns"])

		# legend anchor coordinate 
		object_panelDB.set_item(tuple_legend_panel_indices,
			"legend_anchor_coordinate", dict_user_input["legend_anchor_coordinate"])
		
		# list of legend labels 
		object_panelDB.append_item(tuple_legend_panel_indices, 
			"list_legend_labels", dict_user_input["legend"])

		# list of line objects
		object_panelDB.append_item(tuple_legend_panel_indices,
			"list_line_objects", object_line)

		#----------------------------------------------------------------------------------------------
		# Refine axis properties
		#----------------------------------------------------------------------------------------------
		MpaPlotPropertySingleAxis.refine_single_axis(object_axis_for_panel, object_figure, dict_plot_parameters, 
			user_x_min,
			user_x_max,
			user_y_min,
			user_y_max,
			)
		#----------------------------------------------------------------------------------------------

		ccc += 1 # ==> continue to the next iteration
		#----------------------------------------------------------------------------------------------

	dict_panel_information = object_panelDB.get_dict()

	return (array2D_global_x_min, array2D_global_x_max,
			array2D_global_y_min, array2D_global_y_max,
			dict_panel_information)