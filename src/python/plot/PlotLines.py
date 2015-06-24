"""
Plot one or many lines
Author: Yuhang Wang
Date: 06/18/2015
Usage: python PlotLines.py FILE_LIST-OF-INPUT-DATA-FILE-NAMES FILE_PLOT-PARAMETERS
"""
#================================================
# Use Python 3 style
#================================================
from __future__ import print_function, division
# from __future__ import unicode_literals
#================================================
import matplotlib
import matplotlib.pyplot as Plot 
import sys
import re
import numpy 
import PlotLinesParameters
import pyparsing


#================================================


ccc = 1
file_input_information = sys.argv[ccc]
ccc += 1
file_plot_parameters = sys.argv[ccc]



def is_string(input):
	"""
	Check whether input is a string: plain string or unicode 
	ref: http://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-a-string
	"""
	return isinstance(input,basestring)

def is_convertible_to_list(input):
	"""
	Check whether an input string is convertible to a list
	"""
	if type(input) is str:
		return (re.match(r"\(.+\)", input) is not None)
	else:
		return False

def string_to_bool_or_not(input):
	"""
	Convert a numerical value to boolean
	Convention: "YES" => True
				"NO" => False
				otherwise the original string is returned
	:param str input: either "YES" or "NO"
	"""
	# only proceed when the input type is "str"
	if not is_string(input): return input 

	if input == "YES":
		return True
	elif input == "NO":
		return False
	else:
		return input

def string_to_number_or_not(input):
	"""
	Convert a string to integer | float number 
	:param str input: input data
	:return: either a number or the original input 
	"""
	# only proceed when the input type is "str"
	if type(input) is not str: return input 

	if re.match(r"^\d+$", input):
		return int(float(input))
	elif re.match(r"^\d*\.\d+$", input):
		return float(input)
	else:
		return input


def to_boolean_list_or_not(my_input):
	"""
	convert every element in a list to numerical values if possible
	If not, keep the original value 
	"""	
	output = []	
	if type(my_input) is list:
		for item in my_input:
			output.append(to_boolean_list_or_not(item))
		return output
	else:
		return string_to_bool_or_not(my_input)


def to_numerical_list_or_not(my_input):
	"""
	convert every element in a list to numerical values if possible
	If not, keep the original value 
	"""	
	output = []	
	if type(my_input) is list:
		for item in my_input:
			output.append(to_numerical_list_or_not(item))
		return output
	else:
		return string_to_number_or_not(my_input)

def string_to_tuple_or_not(input):
	"""
	convert string to a list 
	"""
	number_float = pyparsing.Word(pyparsing.nums+'.')
	separator = pyparsing.Suppress(',')
	content = pyparsing.Word(pyparsing.alphas) | number_float | separator
	parens = pyparsing.nestedExpr('(', ')', content=content)

	list_result = parens.parseString(input).asList()[0]
	list_result = to_boolean_list_or_not(list_result)
	list_result = to_numerical_list_or_not(list_result)
	list_result = tuple(list_result)
	return list_result

def read_input_information(file_input_information):
	"""
	Read a file containing a list of input file names
	Then put the content of each data file into a list 
	:param file_input_information: file that contains a list of file names 
	:return: a python list of numpy arrays
	"""
	print("======================================================")
	print("  Read input data files and legends")
	print("  File: {0}".format(file_input_information))
	print("======================================================")
	
	dict_input_file_keywords = PlotLinesParameters.InputFileParameters.get_convention()
	list_input_information = []
	with open(file_input_information, 'r') as IN:
		for line in IN:
			line = line.strip()
			tmp_list = line.split(";")

			# remove extra leading/trailing white spaces
			for i in range(len(tmp_list)):
				tmp_list[i] = tmp_list[i].strip()

			# use default values
			dict_default =  PlotLinesParameters.InputFileParameters.get_defaults()
			dict_current_line = dict()
			for key,value in dict_default.items():
				dict_current_line[key] = value

			for item in tmp_list:
				key, value = item.split(":")
				key = key.strip()
				value = value.strip()
				
				# change to internal keyword
				if key in dict_input_file_keywords.keys():
					key = dict_input_file_keywords[key]
				else:
					msg = "ERROR HINT: input keyword not recognized: \"{0}\"".format(key)
					raise UserWarning(msg)

				if is_convertible_to_list(value):
					value = string_to_tuple_or_not(value)
				else:
					value = string_to_bool_or_not(value)
					value = string_to_number_or_not(value)

				dict_current_line[key] = value
				print(key,': ', value)

			dict_current_line["input_data"] = numpy.loadtxt(dict_current_line["file"])
			print("Loading data file: {0}".format(dict_current_line["file"]))
			list_input_information.append(dict_current_line)
	return list_input_information


def read_plot_parameters(file_plot_parameters, dict_convention, dict_default_parameters):
	"""
	Read a file containing a list of plot parameters 
	and put them into a python dictionary.
	:param str file_plot_parameters: name of the file that contains plotting parameters 
	:return: python dictionary
	"""
	print("======================================================")
	print("  Read plotting parameters")
	print("  File: {0}".format(file_plot_parameters))
	print("======================================================")
	
	# Fill up with defaults
	dict_plot_parameters = dict_default_parameters

    # Update parameters based on user's specifications
	with open(file_plot_parameters, 'r') as IN:
		for line in IN:
			line = line.strip()
			key,value = line.split(':')

			key = key.strip()
			value = value.strip()

			# Only record parameters defined in "dict_convention"
			# Otherwise skip the unknown parameters
			if key in dict_convention.keys():
				new_key = dict_convention[key]
			else:
				print("WARNING: you have specified an unknown parameter: \"{0}\"".format(key))
				continue

			# convert to 'raw string literal' to preserve LaTex formating
			value = r"{0}".format(value)

			# check whether string "value" can be converted to boolean
			value = string_to_bool_or_not(value)

			# If not, try to convert it to a number
			value = string_to_number_or_not(value)

			# if "new_key" is "color_order", then convert it a list
			if type(value) is str and is_convertible_to_list(value):
				value = string_to_tuple_or_not(value)

			print("{0} ==> {1}".format(new_key, value))
			dict_plot_parameters[new_key] = value
	print("\n")
	return dict_plot_parameters

def add_title(object_axis, figure_title, title_font_size):
	"""
	Add figure title 
	:param object_axis: matplotlib Axis object
	:param figure_title: title 
	:param title_font_size: font size 
	"""
	object_axis.set_title(figure_title, fontsize=title_font_size)


def add_axis_label(object_axis, axis_name, label_content, label_font_size, label_padding):
	"""
	Add axis labels 
	:param object_axis: a matplotlib Axis object 
	:param axis_name: 'x' or 'y'
	:param label_content: content of the label
	:param label_font_size: font size for the label 
	:param label_padding: padding between label and axis 
	"""
	if re.match(r"x", axis_name):
		object_axis.set_xlabel(label_content, fontsize=label_font_size, labelpad=label_padding)
	elif re.match(r"y", axis_name):
		object_axis.set_ylabel(label_content, fontsize=label_font_size, labelpad=label_padding)
	else:
		msg = "ERROR HINT: 'axis_name' argument should be 'x' or 'y'\n"
		msg += "\tYour 'axis_name' = \"{0}\"".format(axis_name)
		print(msg)
		return

def add_panel_label(object_axis, x, y, 
			panel_label, 
			panel_label_font_size,
			panel_label_horizontal_alignment,
			panel_label_vertical_alignment,
			panel_box_face_color,
			panel_box_edge_color,
			panel_box_opacity,
			panel_box_padding,
			panel_box_line_width,
			panel_box_line_style,
			panel_box_shape,
			):
	"""
	Add a label to the panel 
	:param object object_axis: a matplotlib Axis object
	:param str panel_label: panel label (string)
	:param float x: x coordinate (0-1.0) with 0 for lower left and 1.0 for upper right
	:param float y: y coordinate (0-1.0) with 0 for lower left and 1.0 for upper right
	:param int panel_label_font_size: unit: points 
	:param int panel_label_font_weight: 0-1000
	:param str panel_label_horizontal_alignment: [ "center" | "right" | "left" ]
	:param str panel_label_vertical_alignment: [ "center" | "top" | "bottom" | "baseline" ]
	:param str panel_box_face_color: face color of the panel box (default: 'w'(i.e., white))
	:param str panel_box_edge_color: face color of the panel box (default: 'k'(i.e., black))
	:param float panel_box_opacity: 0-1.0
	:param int panel_box_padding: numerical value (default: 10)
	:param int panel_box_line_width: default: 4
	:param int panel_box_line_style: ["solid" | "dashed" | "dashdot" | "dotted"] default: "solid"
	:param str panel_box_shape: "square"(default) or "round"
	"""
	dict_font_properties = {
		"fontsize":panel_label_font_size,
		}
	dict_panel_box_properties = {
		"boxstyle":"{0},pad={1}".format(panel_box_shape, panel_box_padding),
		"facecolor":panel_box_face_color,
		"edgecolor":panel_box_edge_color,
		"alpha":panel_box_opacity,
		"linewidth":panel_box_line_width,
		"linestyle":panel_box_line_style,
		}
	object_axis.text(x,y, panel_label,
		fontdict=dict_font_properties,
		horizontalalignment=panel_label_horizontal_alignment,
		verticalalignment=panel_label_vertical_alignment,
		fontweight=0,
		transform=object_axis.transAxes, # use axis coordinate instead of the default data coordinate
		bbox=dict_panel_box_properties,
		)

def add_legend(list_line_objects, list_legend_labels,
		use_round_legend_box,
		legend_location, 
		legend_coordinate,
		show_legend_frame=None, 
		legend_frame_opacity=None,
		number_of_legend_columns=1,
		legend_font_size=10, 
		legend_font_weight=0,
		legend_line_width=1,
		legend_marker_scale=2,
		legend_number_of_marker_points=None,
		legend_number_of_scatter_marker_points=None,
		legend_handle_length=None,
		legend_border_padding=None,
		legend_vertical_spacing=None,
		legend_padding_between_handle_and_text=None,
		legend_padding_between_border_and_axes=None,
		legend_column_spacing=None,
		legend_face_color=None,
		legend_edge_color=None,
		):
	"""
	Add legend
	:param list list_line_objects: list of matplotlib Line object
	:param list list_legend_labels: list of legend labels
	:param use_round_legend_box: True or False to decide whether to use round legend box 
	:param legend_location: the legend_location of the lengend within the plot area
	:param legend_coordinate: a tuple of two numbers between 0 and 1, e.g. (0.5, 0.5)
	:param bool show_legend_frame: True or False to decide whether to show legend box frame 
		(default: None, which will take value from legend.frameon rcParam)
	:param float legend_frame_opacity: a number between 0.0 and 1.0 
		(default: None, which means taking value from legend.framealpha rcParam)
	:param int number_legend_columns: number of legend columns (default: 1)
	:param int legend_font_size: font size for the legend
	:param int legend_font_weight: font weight (0-1000)
	:param int legend_line_width: line width for the legend 
	:param int legend_marker_scale: apply a scaling factor to the size of legend marker (relative to the original size)
			(default: 3)
	:param int legend_number_of_marker_points: number of marker samples in the legend 
			(default: None, i.e., use value from "legend.numpoints" in matplotlib's rcParam)	
	:param int legend_number_of_scatter_marker_points: number of marker samples in the legend for scatter plots
			(default: None, i.e., use value from "legend.scatterpoints" in matplotlib's rcParam)
	:param int legend_handle_length: unit: font-size unit 
			(default: None, i.e., use value from "legend.handlelength" in matplotlib's rcParam)
	:param float legend_border_padding: the whitespace between legend and the border in fractional float numbers  
			(default: None, i.e., use value from "legend.borderpad" in matplotlib's rcParam)
	:param float legend_vertical_spacing: the vertical spacing between legend entries (unit: fraction of the font-size )
			(default: None, i.e., use value from "legend.labelspacing" in matplotlib's rcParam)
	:param float legend_padding_between_handle_and_text: unit: fraction of the font size
			(default: None, i.e., use value from "legend.handletextpad" in matplotlib's rcParam)
	:param float legend_padding_between_border_and_axes: unit: fraction of the font-size 
			(default: None, i.e., use value from "legend.borderaxespad" in matplotlib's rcParam)
	:param float legend_column_spacing: spacing between columns; unit: fraction of the font-size
			(default: None, i.e., use value from "legend.columnspacing" in matplotlib's rcParam)
	:param float legend_face_color: legend face color (default: None, i.e., use matplotlib default)
	:param float legend_edge_color: legend edge color (default: None, i.e., use matplotlib default)
	"""
	Plot.legend(list_line_objects, list_legend_labels,
		fancybox=use_round_legend_box,
		loc=legend_location, 
		bbox_to_anchor=legend_coordinate,
		frameon=show_legend_frame,
		framealpha=legend_frame_opacity,
		ncol=number_of_legend_columns,
		fontsize=legend_font_size,
		markerscale=legend_marker_scale,
		numpoints=legend_number_of_marker_points,
		handlelength=legend_handle_length,
		borderpad=legend_border_padding,
		labelspacing=legend_vertical_spacing,
		handletextpad=legend_padding_between_handle_and_text,
		borderaxespad=legend_padding_between_border_and_axes,
		columnspacing=legend_column_spacing,
		)
	object_legend = Plot.gca().get_legend()
	object_legend_lines = object_legend.get_lines() # get all the lines.Line2D instance from the legend
	object_legend_text  = object_legend.get_texts() # get all the text.Text instance from the legend
	Plot.setp(object_legend_lines, linewidth=legend_line_width)
	Plot.setp(object_legend_text, fontweight=legend_font_weight)

	# Change legend face color
	object_legend_frame = object_legend.get_frame() # get the patch.Rectangle instance surrounding the legend
	if legend_face_color is not None:
		object_legend_frame.set_facecolor(legend_face_color)	

	# Change legend edge color
	if legend_face_color is not None:
		object_legend_frame.set_edgecolor(legend_edge_color)	

	return object_legend

def add_grid(object_figure, show_grid, which_ticks="major", which_axis="both",
		grid_line_style='-', 
		grid_line_width=2,
		grid_line_color='k',
		grid_line_opacity=1.0,
		grid_z_order=0):
	"""
	Add grids 
	:param object_figure: matplotlib Figure object
	:param show_grid: True or False
	:param which_tick: "major"(default), "minor" or "both"
	:param which_axis: 'x', 'y' or "both"(default)
	:param grid_line_style: default: '-'
	:param grid_line_width: line width (default: 2)
	:param grid_line_color: line color (default: 'k')
	:param grid_line_opacity: line opacity (default: 1.0)
	:param grid_z_order: grid order along z (any number; default: 0)
	"""
	Plot.grid(show_grid, which_ticks, which_axis, 
		figure=object_figure,
		linestyle=grid_line_style,
		linewidth=grid_line_width,
		color=grid_line_color,
		alpha=grid_line_opacity,
		zorder=grid_z_order)

def refine_ticks(object_axis, which_axis, 
		tick_major_minor_or_both, 
		tick_in_out_or_inout, 
		tick_length, 
		tick_width, 
		tick_label_font_size, 
		tick_label_font_weight,
		tick_color, tick_label_color, 
		tick_label_padding,
		tick_and_label_z_order=0,
		tick_show_top=True,
		tick_show_bottom=True,
		tick_show_left=True,
		tick_show_right=True,
		tick_label_show_top=False,
		tick_label_show_bottom=True,
		tick_label_show_left=True,
		tick_label_show_right=False,
		tick_label_number_of_decimal_places=None,
		tick_reset_old_parameter=False,
		):
	"""
	Refine tick parameters 
	:param object object_axis: matplotlib Axis object 
	:param str which_axis: 'x' | 'y' | "both"
	:param str tick_major_minor_or_both: "major" | "minor" | "both"
	:param str tick_in_out_or_inout: "in" | "out" | "inout" to control whether to put ticks inside, outside the axes or both
	:param str tick_length: tick length (unit: points)
	:param str tick_width: tick width (unit: points)
	:param int tick_label_font_size: tick label font size in unit points or using shorthand strings (e.g. "large")
	:param int tick_label_font_weight: tick label font weight (0-1000)
	:param str tick_color: tick color (any matplotlib color specifications)
	:param str tick_label_color: tick label color (any matplotlib color specifications)
	:param str tick_label_padding: distance between tick marks and tick labels
	:param str tick_and_label_z_order: tick and label z order ] (default: 0)
	:param bool tick_show_top: 	True | False (default: True)
	:param bool tick_show_bottom: 	True | False (default: True) 
	:param bool tick_show_left: 	True | False (default: True) 
	:param bool tick_show_right: 	True | False (default: True) 
	:param bool tick_label_show_top:		True | False (default: False)
	:param bool tick_label_show_bottom:	True | False (default: True)
	:param bool tick_label_show_left:		True | False (default: True)
	:param bool tick_label_show_right:		True | False (default: False)
	:param int tick_label_number_of_decimal_places: number of decimal places in the tick label 
			(default: None, i.e., use the matplotlib default)
	:param bool tick_reset_old_parameter: reset old parameters before using new ones
	"""
	object_axis.tick_params(
		axis=which_axis, 
		which=tick_major_minor_or_both,
		direction=tick_in_out_or_inout,
		length=tick_length,
		width=tick_width,
		color=tick_color,
		labelcolor=tick_label_color,
		pad=tick_label_padding,
		labelsize=tick_label_font_size,
		zorder=tick_and_label_z_order,
		top=tick_show_top,
		bottom=tick_show_bottom,
		left=tick_show_left,
		right=tick_show_right,
		labeltop=tick_label_show_top,
		labelbottom=tick_label_show_bottom,
		labelleft=tick_label_show_left,
		labelright=tick_label_show_right,
		reset=tick_reset_old_parameter,
		)

	# tick label font weight
	ticks_font = matplotlib.font_manager.FontProperties(family='sans-serif', 
		style='normal',
		weight=tick_label_font_weight, 
		stretch='normal')
	if which_axis == 'x' or which_axis == "both":
		object_axis.set_xticklabels(object_axis.get_xticks(), ticks_font, fontweight=0)
	elif which_axis == 'y' or which_axis == "both":
		object_axis.set_yticklabels(object_axis.get_yticks(), ticks_font)


	# make x tick label a formatted string
	if tick_label_number_of_decimal_places is not None:
		def fn_formatter(tick_value, tick_position):
			return "{0:.{1}f}".format(tick_value, tick_label_number_of_decimal_places)
		temp_axis = getattr(object_axis, "get_{0}axis".format(which_axis))()
		temp_axis.set_major_formatter(matplotlib.ticker.FuncFormatter(fn_formatter))


def add_and_refine_legend(list_legend_information,dict_parameters):
	"""
	Add and refine the legends
	:param list_legend_information: a dictionary of dictionaries. 
		The key is the panel ID (i.e., 0, 1, 2, ...);
		The value is a sub-dictionary with keys: "object_axis", "list_line_objects", "list_legend_labels", "legend_coordinate"
	:param dict dict_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = Plot.gca() # store the current axis object
	for dict_legend_parameters in list_legend_information:
		object_axis = dict_legend_parameters["object_axis"]
		list_line_objects = dict_legend_parameters["list_line_objects"]
		list_legend_labels = dict_legend_parameters["list_legend_labels"]
		legend_coordinate = dict_legend_parameters["legend_coordinate"]
		# set new current axis
		print(object_axis)
		Plot.sca(object_axis)
		add_legend(list_line_objects, list_legend_labels, 
			use_round_legend_box = dict_parameters["use_round_legend_box"], 
			legend_location = dict_parameters["legend_location"],
			legend_coordinate = legend_coordinate,
			show_legend_frame = dict_parameters["show_legend_frame"],
			legend_frame_opacity = dict_parameters["legend_frame_opacity"],
			number_of_legend_columns = dict_parameters["number_of_legend_columns"],
			legend_font_size = dict_parameters["legend_font_size"],
			legend_font_weight = dict_parameters["legend_font_weight"],
			legend_line_width = dict_parameters["legend_line_width"],
			legend_marker_scale = dict_parameters["legend_marker_scale"],
			legend_number_of_marker_points = dict_parameters["legend_number_of_marker_points"],
			legend_number_of_scatter_marker_points = dict_parameters["legend_number_of_marker_points"],
			legend_handle_length = dict_parameters["legend_handle_length"],
			legend_border_padding = dict_parameters["legend_border_padding"],
			legend_vertical_spacing = dict_parameters["legend_vertical_spacing"],
			legend_padding_between_handle_and_text = dict_parameters["legend_padding_between_handle_and_text"],
			legend_padding_between_border_and_axes = dict_parameters["legend_padding_between_border_and_axes"],
			legend_column_spacing = dict_parameters["legend_column_spacing"],
			legend_face_color = dict_parameters["legend_face_color"],
			legend_edge_color = dict_parameters["legend_edge_color"],
			)
	
	# reset current axis back to the original
	Plot.sca(object_old_axis_object)

def refine_figure(object_axis, object_figure, dict_parameters):
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


def update_ticks_and_labels(object_axis, x_or_y, axis_min, axis_max, list_new_ticks):
	"""
	Change the ticks and labels to new values 
	:param object object_axis: matplotlib axis object 
	:param str x_or_y: 'x' or 'y'
	:param float axis_min: min of the updated axis 
	:param float axis_max: max of the updated axis
	:param list list_new_ticks: a list of new tick locations e.g., [0, 0.5, 1.5]
	"""
	if x_or_y == 'x':
		object_axis.set_xlim([axis_min,axis_max])
		object_axis.set_xticks(list_new_ticks)
	elif x_or_y == 'y':
		object_axis.set_ylim([axis_min,axis_max])
		object_axis.set_yticks(list_new_ticks)
	else:
		msg = "ERROR HINT: x_or_y argument should be either \"x\" or \"y\"\n"
		msg += "your value of x_or_y = {0}".format(x_or_y)
		print(msg)
		return


def save_figure(object_figure, output_file_name, 
	figure_dpi,
	figure_padding=0.2,
	figure_transparent=False,
	):
	"""
	Save figure 
	:param object object_figure: matplotlib Figure object 
	:param str output_file_name: output file name 
	:param int figure_dpi: figure resolution in DPI unit (dots/inch)
	:param float figure_padding: padding between edge of the canvas and the figure edge (default: 0.2)
	:param float figure_transparent: True | False (default: False)
	"""
	object_figure.savefig(output_file_name, 
		bbox_inches='tight', 
		dpi=figure_dpi, 
		pad_inches=figure_padding,
		transparent=figure_transparent,
		)

def return_smaller(input_1, input_2):
	"""
	Compare two inputs and return the smaller one 
	If one of them is None, return the other input 
	:param number input_1: input 1
	:param number input_2: input 2
	:return: number 
	"""
	if input_1 is None: return input_2
	if input_2 is None: return input_1
	if input_1 > input_2:
		return input_2
	else:
		return input_1

def return_bigger(input_1, input_2):
	"""
	Compare two inputs and return the bigger one 
	If one of them is None, return the other input 
	:param number input_1: input 1
	:param number input_2: input 2
	:return: number 
	"""
	if input_1 is None: return input_2
	if input_2 is None: return input_1
	if input_1 > input_2:
		return input_1
	else:
		return input_2

def set_axis_limits(object_axis, which_axis, new_min, new_max):
	"""
	Set the X axis limits 
	:param object object_axis: matlotlib Axis object 
	:param str which_axis: 'x' or 'y'
	:param float new_min: new min 
	:param float new_max: new max
	"""
	if which_axis == 'x':
		object_axis.set_xlim([new_min,new_max])
	elif which_axis == 'y':
		object_axis.set_ylim([new_min,new_max])
	else:
		return

def plot(list_input_information, dict_parameters):
	"""
	Plot every data series in list_input_information
	:param list list_input_information: a list of dictionaries
	:param dict dict_parameters: a python dictionary of plotting parameters
	:return: object for the current plot
	"""
	print("======================================================")
	print("  Make a plot")
	print("======================================================")

	figureSize=(dict_parameters["figure_length"], dict_parameters["figure_height"])
	dict_legend_information = dict()

	auto_adjust_returning_dimension = False
	object_figure, list_axis_objects = Plot.subplots(nrows=dict_parameters["figure_number_of_rows"],
		ncols=dict_parameters["figure_number_of_columns"],
		figsize=figureSize,
		sharex=dict_parameters["figure_share_x"],
		sharey=dict_parameters["figure_share_y"],
		squeeze=auto_adjust_returning_dimension,
		)
	object_figure.subplots_adjust(hspace=dict_parameters["figure_subplots_vertical_spacing"],
		wspace=dict_parameters['figure_subplots_horizontal_spacing'])

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
	if dict_parameters["figure_title"] is not None:
		add_title(object_extra_axis, dict_parameters["figure_title"], dict_parameters["figure_title_font_size"])

	#----------------------------------------------------------------------------------------------
	#	Axis Label
	#----------------------------------------------------------------------------------------------
	add_axis_label(object_extra_axis, 'x', dict_parameters["x_label"], dict_parameters["x_label_font_size"],
		dict_parameters["x_label_padding"])
	add_axis_label(object_extra_axis, 'y', dict_parameters["y_label"], dict_parameters["y_label_font_size"],
		dict_parameters["y_label_padding"])
	list_colors = dict_parameters["color_order"]
	list_line_objects  = []
	list_legend_labels = []
	ccc = 0
	global_x_min = None 
	global_x_max = None

	last_which_panel = None
	
	#----------------------------------------------------------------------------------------------
	# ========= *** Start Plotting!  *** ================
	#----------------------------------------------------------------------------------------------
	for item in list_input_information:
		data   = item["input_data"]
		legend = item["legend"]
		legend_coordinate = item["legend_coordinate"]
		legend_panel_coordinate = item["legend_panel_coordinate"]
		panel_coordinate = item["panel_coordinate"]
		panel_label = item["panel_label"]
		panel_label_coordinate = item["panel_label_coordinate"]
		file_input = item["file"]



		# if panel_coordinate != last_which_panel:
		# 	# reset counter 
		# 	ccc = 0
		last_which_panel = panel_coordinate

		# line color
		if dict_parameters["use_color_map_cool"]:
			print(ccc)
			line_color = Plot.cm.cool(ccc*10)
			print(line_color)
		else:
			line_color = list_colors[ccc%len(list_colors)]

		# Get X & Y data
		X = data[:,0]
		Y = data[:,1]

		# update global min/max along X
		x_min = numpy.amin(X)
		x_max = numpy.amax(X)
		global_x_min = return_smaller(global_x_min, x_min)
		global_x_max = return_bigger(global_x_max, x_max)



		id_row_panel, id_column_panel = panel_coordinate
		object_axis = list_axis_objects[id_row_panel, id_column_panel]

		print("=====", file_input, id_row_panel, id_column_panel, "==========")

		# Set the current active Axes instance to this axis 
		Plot.sca(object_axis)

		object_line, = object_axis.plot(X,Y, 
			color=line_color,
			alpha=dict_parameters["line_opacity"],
			linestyle=dict_parameters["line_style"],
			)

		#-------------------------------------------------------------
		# set up legend information
		#-------------------------------------------------------------
		if legend_panel_coordinate not in dict_legend_information:
			dict_legend_information[legend_panel_coordinate] = dict()
		id_row_panel, id_column_panel = legend_panel_coordinate
		dict_legend_information[legend_panel_coordinate]["object_axis"] = list_axis_objects[id_row_panel, id_column_panel]
		
		# add new legend label
		if "list_legend_labels" not in dict_legend_information[legend_panel_coordinate].keys():
			dict_legend_information[legend_panel_coordinate]["list_legend_labels"] = []
		dict_legend_information[legend_panel_coordinate]["list_legend_labels"].append(legend)

		# add line object
		if "list_line_objects" not in dict_legend_information[legend_panel_coordinate].keys():
			dict_legend_information[legend_panel_coordinate]["list_line_objects"] = []
		dict_legend_information[legend_panel_coordinate]["list_line_objects"].append(object_line)

		# add legend coordinate
		if "legend_coordinate" not in dict_legend_information[legend_panel_coordinate].keys():
			dict_legend_information[legend_panel_coordinate]["legend_coordinate"] = legend_coordinate



		# make x limits tight
		if dict_parameters["figure_x_limits_tight"]:
			which_axis = 'x'
			set_axis_limits(object_axis, which_axis, x_min, x_max)

		# show noise-filtered-averaged line
		if dict_parameters["show_block_averaged_line"]:
			from scipy import ndimage
			Y_block_averaged = ndimage.filters.uniform_filter(Y, 
				size=dict_parameters["line_block_average_block_size"], 
				mode="nearest")
			object_line, = object_axis.plot(X,Y_block_averaged,
				linewidth=dict_parameters["block_averaged_line_width"],
				color=line_color,
				)

		object_line.set_label(legend)
		list_legend_labels.append(legend)
		list_line_objects.append(object_line)

		#----------------------------------------------------------------------------------------------
		# Grid
		#----------------------------------------------------------------------------------------------
		add_grid(object_figure, 
			dict_parameters["show_grid"],
			dict_parameters["grid_ticks"],
			dict_parameters["grid_axis"],		
			dict_parameters["grid_line_style"],
			dict_parameters["grid_line_width"],
			dict_parameters["grid_line_color"],
			dict_parameters["grid_line_opacity"],
			dict_parameters["grid_z_order"])

		#----------------------------------------------------------------------------------------------
		# Add panel number 
		#----------------------------------------------------------------------------------------------
		if panel_label is not None:
			x_panel_label, y_panel_label = panel_label_coordinate
			add_panel_label(object_axis, x_panel_label, y_panel_label, panel_label,
				dict_parameters["panel_label_font_size"],
				dict_parameters["panel_label_horizontal_alignment"],
				dict_parameters["panel_label_vertical_alignment"],
				dict_parameters["panel_box_face_color"],
				dict_parameters["panel_box_edge_color"],
				dict_parameters["panel_box_opacity"],
				dict_parameters["panel_box_padding"],
				dict_parameters["panel_box_line_width"],
				dict_parameters["panel_box_line_style"],
				dict_parameters["panel_box_shape"],
				)
		
		ccc += 1

	#----------------------------------------------------------------------------------------------
	# Add legend
	#----------------------------------------------------------------------------------------------
	if dict_parameters["legend_on"]:
		add_and_refine_legend(dict_legend_information.values(), dict_parameters)


	#----------------------------------------------------------------------------------------------
	# Set the limits of X axis to match the global_x_min and global_x_max
	#----------------------------------------------------------------------------------------------
	if dict_parameters["figure_use_global_x_limits"]:
		which_axis = 'x'
		for i in range(0,dict_parameters["figure_number_of_rows"]):
			for j in range(0, dict_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i,j]
			set_axis_limits(object_axis,which_axis,global_x_min, global_x_max)

	#----------------------------------------------------------------------------------------------
	# Remove overlapping tick labels
	#----------------------------------------------------------------------------------------------
	# 1. use the (0,0) axis object to get min,max and current labels
	object_axis = list_axis_objects[0,0]
	xmin,xmax = object_axis.get_xlim()
	ymin,ymax = object_axis.get_ylim()
	list_x_tick_labels = object_axis.get_xticks().tolist()
	list_y_tick_labels = object_axis.get_yticks().tolist()

	if dict_parameters["y_tick_label_hide_overlap"]:
		which_axis = 'y'

		if dict_parameters["y_tick_label_hide_first"]:
			list_new_tick_labels = list_y_tick_labels[1:]
		elif dict_parameters["y_tick_label_hide_last"]:
			list_new_tick_labels = list_y_tick_labels[:-1]
		else:
			list_new_tick_labels = list_y_tick_labels

		# remove the first tick label for any subplot above the first row and below the last row
		for i_row in range(1,dict_parameters['figure_number_of_rows']-1):
			for i_column in range(0,dict_parameters["figure_number_of_columns"]):
				object_axis = list_axis_objects[i_row,i_column]
				update_ticks_and_labels(object_axis,which_axis, ymin,ymax,list_new_tick_labels)
		
	if dict_parameters["x_tick_label_hide_overlap"]:
		which_axis = 'x'

		if dict_parameters["x_tick_label_hide_first"]:
			list_new_tick_labels = list_x_tick_labels[1:]
		elif dict_parameters["x_tick_label_hide_last"]:
			list_new_tick_labels = list_x_tick_labels[:-1]
		else:
			list_new_tick_labels = list_x_tick_labels

		# remove the first tick label for any subplot between the first column and the last column
		for i_row in range(0,dict_parameters['figure_number_of_rows']):
			for i_column in range(1,dict_parameters["figure_number_of_columns"]-1):
				object_axis = list_axis_objects[i_row,i_column]
				update_ticks_and_labels(object_axis,which_axis, ymin,ymax,list_new_tick_labels)
		

	#----------------------------------------------------------------------------------------------
	# Refine the figure
	#----------------------------------------------------------------------------------------------
	n_rows, n_columns = numpy.shape(list_axis_objects)
	for i in range(n_rows):
		for j in range(n_columns):
			object_axis = list_axis_objects[i,j]
			object_legend = object_axis.get_legend()
			refine_figure(object_axis, object_figure, dict_parameters)

	return (object_figure, list_axis_objects)


if __name__ == '__main__':
	list_input_information = read_input_information(file_input_information)
	object_plot_parameters = PlotLinesParameters.PlotParameters()

	list_plot_parameters = read_plot_parameters(file_plot_parameters,
						object_plot_parameters.get_convention(),
						object_plot_parameters.get_defaults())

	if list_plot_parameters["use_latex"] is True:
		#------------------------------------------------
		# Use LaTex
		#------------------------------------------------
		matplotlib.rcParams['text.usetex'] = True
		matplotlib.rcParams['text.latex.unicode'] = True
		matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']

	if list_plot_parameters["use_scipy"] is True:
		import scipy

	object_figure, list_axis_objects = plot(list_input_information, list_plot_parameters)

	#-----------------------------------------------------------------
	# Save figure
	#-----------------------------------------------------------------
	save_figure(object_figure, 
		list_plot_parameters["figure_output_file_name"],
		figure_dpi = list_plot_parameters["figure_dpi"],
		figure_padding = list_plot_parameters["figure_padding"],
		figure_transparent = list_plot_parameters["figure_transparent"],
		)
	Plot.show()
