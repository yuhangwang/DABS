"""
MPA PLOT
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
import matplotlib.pyplot
import numpy
#---------------------------------------------------------------
import mpa_plot_ticks      as MpaPlotTicks
import mpa_modifier_axis   as MpaModifierAxis 
import mpa_modifier_legend as MpaModifierLegend   
import mpa_modifier_figure as MpaModifierFigure  
import mpa_toolkit         as MpaTool 
#---------------------------------------------------------------

def _add_common_labels(object_figure, dict_plot_parameters):
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
	

def _refine_each_axis(object_axis, object_figure, dict_plot_parameters, 
	user_x_min,
	user_x_max,
	user_y_min,
	user_y_max,
	panel_label_coordinate,
	panel_label,
	):
	"""
	Refine each axis 
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

	#----------------------------------------------------------------------------------------------
	# Add panel number 
	#----------------------------------------------------------------------------------------------
	if panel_label is not None:
		x, y = panel_label_coordinate
	 	MpaModifierAxis.add_panel_label(object_axis, x, y, panel_label,
			dict_plot_parameters["panel_label_font_size"],
			dict_plot_parameters["panel_label_horizontal_alignment"],
			dict_plot_parameters["panel_label_vertical_alignment"],
			dict_plot_parameters["panel_box_face_color"],
			dict_plot_parameters["panel_box_edge_color"],
			dict_plot_parameters["panel_box_opacity"],
			dict_plot_parameters["panel_box_padding"],
			dict_plot_parameters["panel_box_line_width"],
			dict_plot_parameters["panel_box_line_style"],
			dict_plot_parameters["panel_box_shape"],
			)


def _refine_all_axes(object_figure, list_axis_objects, dict_plot_parameters, dict_legend_information,
	array2D_global_x_min,
	array2D_global_x_max,
	array2D_global_y_min,
	array2D_global_y_max,
	):
	"""
	Refine properties for all axes 
	:param list list_axis_objects: list of axis objects 
	:param dict dict_plot_parameters: plot parameter dictionary
	:param dict dict_legend_information: legend information dictionary
	:param list array2D_global_x_min: a 2D list of global x minimum for every axis 
	:param list array2D_global_x_max: a 2D list of global x maximum for every axis 
	:param list array2D_global_y_min: a 2D list of global y minimum for every axis 
	:param list array2D_global_y_max: a 2D list of global y maximum for every axis 
	"""

	#----------------------------------------------------------------------------------------------
	# Add common labels
	#----------------------------------------------------------------------------------------------
	_add_common_labels(object_figure, dict_plot_parameters)

	#----------------------------------------------------------------------------------------------
	# Add legend
	#----------------------------------------------------------------------------------------------
	if dict_plot_parameters["legend_on"]:
		MpaModifierLegend.add_and_refine_legend(dict_legend_information.values(), dict_plot_parameters)

	#----------------------------------------------------------------------------------------------
	# Make axis limits tight
	#----------------------------------------------------------------------------------------------
	MpaPlotTicks.make_all_axis_limits_tight(list_axis_objects, dict_plot_parameters,
		array2D_global_x_min,
		array2D_global_x_max,
		array2D_global_y_min,
		array2D_global_y_max,
		)

	#----------------------------------------------------------------------------------------------
	# Remove overlapping tick labels
	#----------------------------------------------------------------------------------------------
	MpaPlotTicks.hide_tick_label_overlap(list_axis_objects, dict_plot_parameters)
	
	#----------------------------------------------------------------------------------------------
	# Refine the figure ticks
	#----------------------------------------------------------------------------------------------
	MpaPlotTicks.refine_ticks_all_axes(list_axis_objects, object_figure, dict_plot_parameters)


def plot(list_input_information, dict_plot_parameters):
	"""
	Plot every data series in list_input_information
	
	:param list list_input_information: a list of dictionaries
	:param dict dict_plot_parameters: a python dictionary of plotting parameters
	:return: object for the current plot
	"""
	#-------------------------------------------------------------------
	# Manage external dependencies
	#-------------------------------------------------------------------
	#---------------------------------------------------
	#		Dependency: Latex
	#---------------------------------------------------
	if dict_plot_parameters["use_latex"] is True:
		matplotlib.rcParams['text.usetex'] = True
		matplotlib.rcParams['text.latex.unicode'] = True
		matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']
	#---------------------------------------------------
	#		Dependency: SciPy
	#---------------------------------------------------
	if dict_plot_parameters["use_scipy"] is True:
		import scipy
	#-------------------------------------------------------------------

	#-------------------------------------------------------------------
	# Create a list of figure/axis objects 
	#-------------------------------------------------------------------
	figureSize=(dict_plot_parameters["figure_length"], dict_plot_parameters["figure_height"])
	dict_legend_information = dict()

	auto_adjust_returning_dimension = False
	object_figure, list_axis_objects = matplotlib.pyplot.subplots(nrows=dict_plot_parameters["figure_number_of_rows"],
		ncols=dict_plot_parameters["figure_number_of_columns"],
		figsize=figureSize,
		sharex=dict_plot_parameters["figure_share_x"],
		sharey=dict_plot_parameters["figure_share_y"],
		squeeze=auto_adjust_returning_dimension,
		)

	object_figure.subplots_adjust(hspace=dict_plot_parameters["figure_subplots_vertical_spacing"],
		wspace=dict_plot_parameters['figure_subplots_horizontal_spacing'])


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
	# ========= *** Start Plotting!  *** ================
	#----------------------------------------------------------------------------------------------
	list_colors = dict_plot_parameters["color_order"]
	list_line_objects  = []
	list_legend_labels = []
	ccc = 0
	last_which_panel = None
	for item in list_input_information:
		data   = item["input_data"]
		legend = item["legend"]
		legend_anchor_coordinate = item["legend_anchor_coordinate"]
		legend_panel_indices = item["legend_panel_indices"]
		panel_indices = item["panel_indices"]
		panel_label = item["panel_label"]
		panel_label_coordinate = item["panel_label_coordinate"]
		file_input = item["file"]
		user_x_min = item["x_min"]
		user_x_max = item["x_max"]
		user_y_min = item["y_min"]
		user_y_max = item["y_max"]

		# set line color
		if dict_plot_parameters["use_color_map_cool"]:
			print(ccc)
			line_color = matplotlib.pyplot.cm.cool(ccc*10)
			print(line_color)
		else:
			line_color = list_colors[ccc%len(list_colors)]

		# Get X & Y data
		X = data[:,0]
		Y = data[:,1]

		panel_id_row, panel_id_column = panel_indices
		object_axis = list_axis_objects[panel_id_row, panel_id_column]

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
		matplotlib.pyplot.sca(object_axis)

		#-------------------------------------------------
		#  Plot!
		#-------------------------------------------------
		object_line, = object_axis.plot(X,Y, 
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
				size=dict_plot_parameters["line_block_average_block_size"], 
				mode="nearest")
			object_line, = object_axis.plot(X,Y_block_averaged,
				linewidth=dict_plot_parameters["block_averaged_line_width"],
				color=line_color,
				)

		#-------------------------------------------------------------
		# set up legend information
		#-------------------------------------------------------------
		if legend_panel_indices not in dict_legend_information:
			dict_legend_information[legend_panel_indices] = dict() # use tuple as the dictionary key
		panel_id_row, panel_id_column = legend_panel_indices
		dict_legend_information[legend_panel_indices]["object_axis"] = list_axis_objects[panel_id_row, panel_id_column]
		
		# add new legend label
		if "list_legend_labels" not in dict_legend_information[legend_panel_indices].keys():
			dict_legend_information[legend_panel_indices]["list_legend_labels"] = []
		dict_legend_information[legend_panel_indices]["list_legend_labels"].append(legend)

		# add line object
		if "list_line_objects" not in dict_legend_information[legend_panel_indices].keys():
			dict_legend_information[legend_panel_indices]["list_line_objects"] = []
		dict_legend_information[legend_panel_indices]["list_line_objects"].append(object_line)

		# add legend coordinate
		if "legend_anchor_coordinate" not in dict_legend_information[legend_panel_indices].keys():
			dict_legend_information[legend_panel_indices]["legend_anchor_coordinate"] = legend_anchor_coordinate

		#----------------------------------------------------------------------------------------------
		# Refine axis properties
		#----------------------------------------------------------------------------------------------
		_refine_each_axis(object_axis, object_figure, dict_plot_parameters, 
			user_x_min,
			user_x_max,
			user_y_min,
			user_y_max,
			panel_label_coordinate,
			panel_label,
			)

		#----------------------------------------------------------------------------------------------
		object_line.set_label(legend)
		list_legend_labels.append(legend)
		list_line_objects.append(object_line)
		ccc += 1
		#----------------------------------------------------------------------------------------------
	#====================================================================================================
	
	#----------------------------------------------------------------------------------------------
	# Refine properties for all axes
	#----------------------------------------------------------------------------------------------
	_refine_all_axes(object_figure, list_axis_objects, dict_plot_parameters, dict_legend_information,
		array2D_global_x_min,
		array2D_global_x_max,
		array2D_global_y_min,
		array2D_global_y_max,
		)

	return (object_figure, list_axis_objects)
