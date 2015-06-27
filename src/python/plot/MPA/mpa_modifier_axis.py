"""
MPA AXIS MODIFIER
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
#-------------------------------------------------
import re
#-------------------------------------------------
import matplotlib.pyplot
#-------------------------------------------------

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
	matplotlib.pyplot.grid(show_grid, which_ticks, which_axis, 
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


def update_ticks_and_labels(object_axis, x_or_y, list_new_ticks):
	"""
	Change the ticks and labels to new values 
	:param object object_axis: matplotlib axis object 
	:param str x_or_y: 'x' or 'y'
	:param list list_new_ticks: a list of new tick locations e.g., [0, 0.5, 1.5]
	"""
	# Developers' note:
	# In the new Matplotlib, "ticks" and "lim" are related but not in sync.
	# For example, the xlim can be [1,3], but the xticks can be [0,1,2,3,4]
	# This means if xticks can have more information than what is set in xlim.
	# Therefore is you want to remove the first/last element of the ticks,
	# you must also set the lim to be the same as before.
	# This is why I have to call "set_xlim()".
	if x_or_y == 'x':
		old_x_min, old_x_max = object_axis.get_xlim()
		object_axis.set_xticks(list_new_ticks)
		object_axis.set_xlim([old_x_min, old_x_max]) # make sure xlim is unchanged
	elif x_or_y == 'y':
		old_y_min, old_y_max = object_axis.get_ylim()
		object_axis.set_yticks(list_new_ticks)
		object_axis.set_ylim([old_y_min, old_y_max])
	else:
		msg = "ERROR HINT: x_or_y argument should be either \"x\" or \"y\"\n"
		msg += "your value of x_or_y = {0}".format(x_or_y)
		print(msg)
		return


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
