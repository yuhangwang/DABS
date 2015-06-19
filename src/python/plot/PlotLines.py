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
#================================================
import matplotlib.pyplot as Plot 
import sys
import re
import numpy 
import PlotLinesParameters

#------------------------------------------------
# LaTex
#------------------------------------------------
import matplotlib
matplotlib.rcParams['text.usetex']=True
matplotlib.rcParams['text.latex.unicode']=True
#------------------------------------------------

#================================================


ccc = 1
file_listInputDataFiles = sys.argv[ccc]
ccc += 1
file_plotParameters = sys.argv[ccc]




def string_to_bool_or_not(YES_or_NO):
	"""
	Convert a numerical value to boolean
	Convention: "YES" => True
				"NO" => False
				otherwise the original string is returned
	:param str YES_or_NO: either "YES" or "NO"
	"""
	if YES_or_NO == "YES":
		return True
	elif YES_or_NO == "NO":
		return False
	else:
		return YES_or_NO

def string_to_number_or_not(string):
	"""
	Convert a string to integer | float number 
	:param str string: input string 
	:return: either a number or the original string 
	"""
	if re.match(r"^\d+$", string):
		return int(float(string))
	elif re.match(r"^\d*\.\d+$", string):
		return float(string)
	else:
		return string


def read_data(file_listInputDataFiles):
	"""
	Read a file containing a list of input file names
	Then put the content of each data file into a list 
	:param file_listInputDataFiles: file that contains a list of file names 
	:return: a python list of numpy arrays
	"""
	print("======================================================")
	print("  Read input data files and legends")
	print("  File: {0}".format(file_listInputDataFiles))
	print("======================================================")
	list_data_and_legend = []
	with open(file_listInputDataFiles, 'r') as IN:
		for line in IN:
			line = line.strip()
			file_name, legend = line.split(";")
			file_name = file_name.strip()
			legend = legend.strip()
			data = numpy.loadtxt(file_name)
			print("Loading data from: {0}\t{1}\t[{2}]".format(file_name, data.shape, legend))
			list_data_and_legend.append([data, legend])
	print("\n")
	return list_data_and_legend

def read_plot_parameters(file_plotParameters, dict_convention, dict_default_parameters):
	"""
	Read a file containing a list of plot parameters 
	and put them into a python dictionary.
	:param str file_plotParameters: name of the file that contains plotting parameters 
	:return: python dictionary
	"""
	print("======================================================")
	print("  Read plotting parameters")
	print("  File: {0}".format(file_plotParameters))
	print("======================================================")
	
	# Fill up with defaults
	dict_plot_parameters = dict_default_parameters

    # Update parameters based on user's specifications
	with open(file_plotParameters, 'r') as IN:
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

			print("\"{0}\"\t\"{1}\"".format(new_key, value))

			# convert to 'raw string literal' to preserve LaTex formating
			value = r"{0}".format(value)
			dict_plot_parameters[new_key] = string_to_number_or_not(string_to_bool_or_not(value))
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


def add_axis_label(object_axis, axis_name, label_content, label_font_size):
	"""
	Add axis labels 
	:param object_axis: a matplotlib Axis object 
	:param axis_name: 'x' or 'y'
	:param label_content: content of the label
	:param label_font_size: font size for the label 
	"""
	if re.match(r"x", axis_name):
		object_axis.set_xlabel(label_content, fontsize=label_font_size)
	elif re.match(r"y", axis_name):
		object_axis.set_ylabel(label_content, fontsize=label_font_size)
	else:
		msg = "ERROR HINT: 'axis_name' argument should be 'x' or 'y'\n"
		msg += "\tYour 'axis_name' = \"{0}\"".format(axis_name)
		print(msg)
		return
	
def add_legend(object_axis, 
		use_round_legend_box,
		legend_location, 
		legend_box_anchor_coordinate_tuple,
		show_legend_frame=None, 
		legend_frame_alpha=None,
		number_of_legend_columns=1,
		legend_font_size=10, 
		legend_handle_length=None,
		legend_border_padding=None,
		legend_vertical_spacing=None,
		):
	"""
	Add legend
	:param object_axis: matplotlib Axis object 
	:param use_round_legend_box: True or False to decide whether to use round legend box 
	:param legend_location: the legend_location of the lengend within the plot area
	:param legend_box_anchor_coordinate_tuple: a tuple of two numbers between 0 and 1, e.g. (0.5, 0.5)
	:param bool show_legend_frame: True or False to decide whether to show legend box frame 
		(default: None, which will take value from legend.frameon rcParam)
	:param float legend_frame_alpha: a number between 0.0 and 1.0 
		(default: None, which means taking value from legend.framealpha rcParam)
	:param int number_legend_columns: number of legend columns (default: 1)
	:param int legend_font_size: font size for the legend
	:param int legend_handle_length: unit: font-size unit 
			(default: None, i.e., use value from "legend.handlelength" in matplotlib's rcParam)
	:param float legend_border_padding: the whitespace between legend and the border in fractional float numbers  
			(default: None, i.e., use value from "legend.borderpad" in matplotlib's rcParam)
	:param float legend_vertical_spacing: the vertical spacing between legend entries (unit: fraction of font-size units)
			(default: None, i.e., use value from "legend.labelspacing" in matplotlib's rcParam)
	"""
	Plot.legend(fancybox=use_round_legend_box,
		loc=legend_location, 
		bbox_to_anchor=legend_box_anchor_coordinate_tuple,
		frameon=show_legend_frame,
		framealpha=legend_frame_alpha,
		ncol=number_of_legend_columns,
		fontsize=legend_font_size,
		handlelength=legend_handle_length,
		borderpad=legend_border_padding,
		labelspacing=legend_vertical_spacing,
		)

def add_grid(object_figure, show_grid, which_ticks="major", which_axis="both",
		grid_line_style='-', 
		grid_line_width=2,
		grid_line_color='k',
		grid_line_alpha=1.0,
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
	:param grid_line_alpha: line transparency (default: 1.0)
	:param grid_z_order: grid order along z (any number; default: 0)
	"""
	Plot.grid(show_grid, which_ticks, which_axis, 
		figure=object_figure,
		linestyle=grid_line_style,
		linewidth=grid_line_width,
		color=grid_line_color,
		alpha=grid_line_alpha,
		zorder=grid_z_order)

def refine_ticks(object_axis, which_axis, tick_major_minor_or_both, tick_in_out_or_inout, 
		tick_length, tick_width, tick_label_font_size,
		tick_color, tick_label_color, tick_label_padding,
		tick_and_label_z_order=0,
		tick_show_top=True,
		tick_show_bottom=True,
		tick_show_left=True,
		tick_show_right=True,
		tick_label_show_top=False,
		tick_label_show_bottom=True,
		tick_label_show_left=True,
		tick_label_show_right=False,
		tick_reset_old_parameters=False,
		):
	"""
	Refine tick parameters 
	:param object object_axis: matplotlib Axis object 
	:param str which_axis: 'x' | 'y' | "both"
	:param str tick_major_minor_or_both: "major" | "minor" | "both"
	:param str tick_in_out_or_inout: "in" | "out" | "inout" to control whether to put ticks inside, outside the axes or both
	:param str tick_length: tick length (unit: points)
	:param str tick_width: tick width (unit: points)
	:param str tick_label_font_size: tick label font size in unit points | using shorthand strings (e.g. "large")
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
	:param bool tick_reset_old_parameters: reset old parameters before using new ones
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
		reset=tick_reset_old_parameters,
		)

def plot(list_data_and_legend, dict_parameters):
	"""
	Plot every data series in list_data_and_legend
	:param list list_data_and_legend: a list of data arrays|numpy arrays
	:param dict dict_parameters: a python dictionary of plotting parameters
	:return: object for the current plot
	"""
	print("======================================================")
	print("  Make a plot")
	print("======================================================")

	figureSize=(dict_parameters["figure_length"], dict_parameters["figure_height"])

	object_figure, object_axis = Plot.subplots(nrows=1,ncols=1,figsize=figureSize,
		sharex=False,sharey=False,
		squeeze=True,subplot_kw=None,gridspec_kw=None,
		)

	for list_data_and_legend in list_data_and_legend:
		data, legend = list_data_and_legend
		X = data[:,0]
		Y = data[:,1]
		object_plot, = object_axis.plot(X,Y,
			linestyle=dict_parameters["lineStyle"])
		object_plot.set_label(legend)

	#----------------------------------------------------------------------------------------------
	# Figure title
	#----------------------------------------------------------------------------------------------
	add_title(object_axis, dict_parameters["figure_title"], dict_parameters["figure_title_font_size"])

	#----------------------------------------------------------------------------------------------
	# 	Axis Label
	#----------------------------------------------------------------------------------------------
	add_axis_label(object_axis, 'x', dict_parameters["xLabel"], dict_parameters["xLabel_fontSize"])
	add_axis_label(object_axis, 'y', dict_parameters["yLabel"], dict_parameters["yLabel_fontSize"])

	#----------------------------------------------------------------------------------------------
	# 	Legend
	#----------------------------------------------------------------------------------------------
	add_legend(object_axis, 
		use_round_legend_box = dict_parameters["use_round_legend_box"], 
		legend_location = dict_parameters["legend_location"],
		legend_box_anchor_coordinate_tuple = dict_parameters["legend_box_anchor_coordinate_tuple"],
		show_legend_frame = dict_parameters["show_legend_frame"],
		legend_frame_alpha = dict_parameters["legend_frame_alpha"],
		number_of_legend_columns = dict_parameters["number_of_legend_columns"],
		legend_font_size = dict_parameters["legend_font_size"],
		legend_handle_length = dict_parameters["legend_handle_length"],
		legend_border_padding = dict_parameters["legend_border_padding"],
		legend_vertical_spacing = dict_parameters["legend_vertical_spacing"],
		)

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
		dict_parameters["grid_line_alpha"],
		dict_parameters["grid_z_order"])

	#----------------------------------------------------------------------------------------------
	# X Tick 
	#----------------------------------------------------------------------------------------------
	for which_axis in ['x','y']:
		refine_ticks(object_axis, which_axis, 
			tick_major_minor_or_both = dict_parameters[which_axis+"_tick_major_minor_or_both"], 
			tick_in_out_or_inout = dict_parameters[which_axis+"_tick_in_out_or_inout"], 
			tick_length = dict_parameters[which_axis+"_tick_length"], 
			tick_width = dict_parameters[which_axis+"_tick_width"], 
			tick_label_font_size = dict_parameters[which_axis+"_tick_label_font_size"],
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
			tick_reset_old_parameters = dict_parameters[which_axis+"_tick_reset_old_parameters"],
			)
	return (object_figure, object_axis)



if __name__ == '__main__':
	list_data_and_legend = read_data(file_listInputDataFiles)
	object_plot_parameters = PlotLinesParameters.PlotParameters()
	list_plot_parameters = read_plot_parameters(file_plotParameters,
						object_plot_parameters.get_convention(),
						object_plot_parameters.get_defaults())
	plot(list_data_and_legend, list_plot_parameters)
	Plot.show()
