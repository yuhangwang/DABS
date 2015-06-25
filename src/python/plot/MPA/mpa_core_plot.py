"""
MPA PLOT
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
from mpa_plot_refine_ticks import plot_refine_ticks as MPA_refine_ticks
#---------------------------------------------------------------

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

	figureSize=(dict_plot_parameters["figure_length"], dict_plot_parameters["figure_height"])
	dict_legend_information = dict()

	print(" ======== share y", dict_plot_parameters["figure_share_y"])
	auto_adjust_returning_dimension = False
	object_figure, list_axis_objects = Plot.subplots(nrows=dict_plot_parameters["figure_number_of_rows"],
		ncols=dict_plot_parameters["figure_number_of_columns"],
		figsize=figureSize,
		sharex=dict_plot_parameters["figure_share_x"],
		sharey=dict_plot_parameters["figure_share_y"],
		squeeze=auto_adjust_returning_dimension,
		)
	object_figure.subplots_adjust(hspace=dict_plot_parameters["figure_subplots_vertical_spacing"],
		wspace=dict_plot_parameters['figure_subplots_horizontal_spacing'])

	#----------------------------------------------------------
	# make an extra axis just to show the common X/Y label
	#----------------------------------------------------------
	object_extra_axis = object_figure.add_subplot(1,1,1)
	object_extra_axis.patch.set_alpha(0.)

	# turn off the extra axis's tick labels
	Plot.setp(object_extra_axis.get_xticklabels(), visible=False)
	Plot.setp(object_extra_axis.get_yticklabels(), visible=False)
	object_extra_axis.set_xticks([])
	object_extra_axis.set_yticks([])

	# Make the frame line transparent
	for child in object_extra_axis.get_children():
		if isinstance(child, matplotlib.spines.Spine):
			child.set_color((0,0,0,0))

	# Figure title
	if dict_plot_parameters["figure_title"] is not None:
		add_title(object_extra_axis, dict_plot_parameters["figure_title"], dict_plot_parameters["figure_title_font_size"])

	#----------------------------------------------------------------------------------------------
	#	Axis Label
	#----------------------------------------------------------------------------------------------
	add_axis_label(object_extra_axis, 'x', dict_plot_parameters["x_label"], dict_plot_parameters["x_label_font_size"],
		dict_plot_parameters["x_label_padding"])
	add_axis_label(object_extra_axis, 'y', dict_plot_parameters["y_label"], dict_plot_parameters["y_label_font_size"],
		dict_plot_parameters["y_label_padding"])
	list_colors = dict_plot_parameters["color_order"]
	list_line_objects  = []
	list_legend_labels = []
	ccc = 0


	#----------------------------------------------------------------------------------------------
	# make a 2D array to store the global min/max for each figure axis
	#----------------------------------------------------------------------------------------------
	array2D_global_x_min = []
	array2D_global_x_max = []
	array2D_global_y_min = []
	array2D_global_y_max = []
	for i_row in range(0,dict_plot_parameters["figure_number_of_rows"]):
		array2D_global_x_min.append([])
		array2D_global_x_max.append([])
		array2D_global_y_min.append([])
		array2D_global_y_max.append([])
		for i_column in range(0, dict_plot_parameters["figure_number_of_columns"]):
			array2D_global_x_min[i_row].append(None)
			array2D_global_x_max[i_row].append(None)
			array2D_global_y_min[i_row].append(None)
			array2D_global_y_max[i_row].append(None)

	
	#----------------------------------------------------------------------------------------------
	# ========= *** Start Plotting!  *** ================
	#----------------------------------------------------------------------------------------------
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


		# if panel_indices != last_which_panel:
		# 	# reset counter 
		# 	ccc = 0
		last_which_panel = panel_indices

		# line color
		if dict_plot_parameters["use_color_map_cool"]:
			print(ccc)
			line_color = Plot.cm.cool(ccc*10)
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
		array2D_global_x_min[panel_id_row][panel_id_column] = return_smaller(array2D_global_x_min[panel_id_row][panel_id_column], x_min)
		array2D_global_x_max[panel_id_row][panel_id_column] = return_bigger(array2D_global_x_max[panel_id_row][panel_id_column], x_max)
		array2D_global_y_min[panel_id_row][panel_id_column] = return_smaller(array2D_global_y_min[panel_id_row][panel_id_column], y_min)
		array2D_global_y_max[panel_id_row][panel_id_column] = return_bigger(array2D_global_y_max[panel_id_row][panel_id_column], y_max)


		if panel_indices == (1,0):
			print("=== y_min: {0} y_max: {1}".format(y_min,y_max))

		# Set the current active Axes instance to this axis 
		Plot.sca(object_axis)

		object_line, = object_axis.plot(X,Y, 
			color=line_color,
			alpha=dict_plot_parameters["line_opacity"],
			linestyle=dict_plot_parameters["line_style"],
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


		#-------------------------------------------------------------
		# Use user-defined x limits
		#-------------------------------------------------------------
		if dict_plot_parameters["figure_x_limits_user_defined"]:
			x_min, x_max = object_axis.get_xlim()
			if user_x_min is not None:
				x_min = user_x_min
				object_axis.set_xlim([x_min, x_max])
			if user_x_max is not None:
				x_max = user_x_max 
				object_axis.set_xlim([x_min, x_max])
		
		#-------------------------------------------------------------
		# Use user-defined y limits
		#-------------------------------------------------------------
		if dict_plot_parameters["figure_y_limits_user_defined"]:
			y_min, y_max = object_axis.get_ylim()
			if user_y_min is not None:
				y_min = user_y_min
				object_axis.set_ylim([y_min, y_max])
			if user_y_max is not None:
				y_max = user_y_max 
				object_axis.set_ylim([y_min, y_max])
			

		#-------------------------------------------------------------
		# show noise-filtered-averaged line
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

		object_line.set_label(legend)
		list_legend_labels.append(legend)
		list_line_objects.append(object_line)


		#----------------------------------------------------------------------------------------------
		# Grid
		#----------------------------------------------------------------------------------------------
		add_grid(object_figure, 
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
			x_panel_label, y_panel_label = panel_label_coordinate
			add_panel_label(object_axis, x_panel_label, y_panel_label, panel_label,
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
		
		ccc += 1

	#----------------------------------------------------------------------------------------------
	# Add legend
	#----------------------------------------------------------------------------------------------
	if dict_plot_parameters["legend_on"]:
		add_and_refine_legend(dict_legend_information.values(), dict_plot_parameters)

	#-------------------------------------------------------------
	# make x limits tight
	#-------------------------------------------------------------
	if dict_plot_parameters["figure_x_limits_tight"]:
		which_axis = 'x'
		for panel_id_row in range(0, dict_plot_parameters["figure_number_of_rows"]):
			for panel_id_column in range(0, dict_plot_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[panel_id_row, panel_id_column]
				set_axis_limits(object_axis, 
					which_axis, 
					array2D_global_x_min[panel_id_row][panel_id_column],
					array2D_global_x_max[panel_id_row][panel_id_column],
					)
	#-------------------------------------------------------------
	# make y limits tight
	#-------------------------------------------------------------
	if dict_plot_parameters["figure_y_limits_tight"]:
		which_axis = 'y'
		for panel_id_row in range(0, dict_plot_parameters["figure_number_of_rows"]):
			for panel_id_column in range(0, dict_plot_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[panel_id_row, panel_id_column]
				set_axis_limits(object_axis, 
					which_axis, 
					array2D_global_y_min[panel_id_row][panel_id_column],
					array2D_global_y_max[panel_id_row][panel_id_column],
					)

	#----------------------------------------------------------------------------------------------
	# Remove overlapping tick labels
	#----------------------------------------------------------------------------------------------
	# 1. use the (0,0) axis object to get min,max and current labels

	if dict_plot_parameters["y_tick_label_hide_overlap"]:
		# remove the first tick label for all but the last row of subplots
		which_axis = 'y'
		for i_row in range(0,dict_plot_parameters['figure_number_of_rows']-1):
			for i_column in range(0,dict_plot_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i_row,i_column]
				list_y_tick_labels = object_axis.get_yticks().tolist()		
				if dict_plot_parameters["y_tick_label_hide_first"]:
					list_new_tick_labels = list_y_tick_labels[1:]
				elif dict_plot_parameters["y_tick_label_hide_last"]:
					list_new_tick_labels = list_y_tick_labels[:-1]
				else:
					list_new_tick_labels = list_y_tick_labels
				update_ticks_and_labels(object_axis,which_axis, list_new_tick_labels)
		
	if dict_plot_parameters["x_tick_label_hide_overlap"]:
		# remove the first tick label for all but the first column of subplots
		which_axis = 'x'
		for i_row in range(0,dict_plot_parameters['figure_number_of_rows']):
			for i_column in range(1,dict_plot_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i_row,i_column]
				list_x_tick_labels = object_axis.get_xticks().tolist()

				if dict_plot_parameters["x_tick_label_hide_first"]:
					list_new_tick_labels = list_x_tick_labels[1:]
				elif dict_plot_parameters["x_tick_label_hide_last"]:
					list_new_tick_labels = list_x_tick_labels[:-1]
				else:
					list_new_tick_labels = list_x_tick_labels
				update_ticks_and_labels(object_axis,which_axis, list_new_tick_labels)
		

	#----------------------------------------------------------------------------------------------
	# Refine the figure
	#----------------------------------------------------------------------------------------------
	n_rows, n_columns = numpy.shape(list_axis_objects)
	for i in range(n_rows):
		for j in range(n_columns):
			object_axis = list_axis_objects[i,j]
			object_legend = object_axis.get_legend()
			MPA_refine_ticks(object_axis, object_figure, dict_plot_parameters)

	return (object_figure, list_axis_objects)
