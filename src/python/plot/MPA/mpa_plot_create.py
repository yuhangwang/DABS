"""
MPA PLOT: create figure & axis objects
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------------------
from __future__ import print_function, division
#---------------------------------------------------------------
import matplotlib.pyplot
#---------------------------------------------------------------

def figure(dict_plot_parameters):
	"""
	Create matplotlib figure & axis objects 
	:param dict dict_plot_parameters: an MPA dictionary of plot parameters 
	:return: (object_figure, list_axis_objects)
	"""
	figureSize=(dict_plot_parameters["figure_length"], dict_plot_parameters["figure_height"])

	auto_adjust_returning_dimension = False
	object_figure, list_axis_objects = matplotlib.pyplot.subplots(
		nrows=dict_plot_parameters["figure_number_of_rows"],
		ncols=dict_plot_parameters["figure_number_of_columns"],
		figsize=figureSize,
		sharex=dict_plot_parameters["figure_share_x"],
		sharey=dict_plot_parameters["figure_share_y"],
		squeeze=auto_adjust_returning_dimension,
		)

	object_figure.subplots_adjust(hspace=dict_plot_parameters["figure_subplots_vertical_spacing"],
		wspace=dict_plot_parameters['figure_subplots_horizontal_spacing'])

	return (object_figure, list_axis_objects)
