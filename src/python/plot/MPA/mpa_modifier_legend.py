"""
MPA LEGEND MODIFIER
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""


def add_legend(list_line_objects, list_legend_labels,
		use_round_legend_box,
		legend_at_which_figure_corner, 
		legend_anchor_coordinate,
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
	:param legend_at_which_figure_corner: i.e., "upper left" | "upper right" | "lower left" | "lower right" | "best"
	:param legend_anchor_coordinate: a tuple of two numbers between 0 and 1, e.g. (0.5, 0.5)
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
		loc=legend_at_which_figure_corner, 
		bbox_to_anchor=legend_anchor_coordinate,
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

def add_and_refine_legend(list_legend_information,dict_parameters):
	"""
	Add and refine the legends
	:param list_legend_information: a dictionary of dictionaries. 
		The key is the panel ID (i.e., 0, 1, 2, ...);
		The value is a sub-dictionary with keys: "object_axis", "list_line_objects", "list_legend_labels", "legend_anchor_coordinate"
	:param dict dict_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = Plot.gca() # store the current axis object
	for dict_legend_parameters in list_legend_information:
		object_axis = dict_legend_parameters["object_axis"]
		list_line_objects = dict_legend_parameters["list_line_objects"]
		list_legend_labels = dict_legend_parameters["list_legend_labels"]
		legend_anchor_coordinate = dict_legend_parameters["legend_anchor_coordinate"]
		# set new current axis
		print(object_axis)
		Plot.sca(object_axis)
		add_legend(list_line_objects, list_legend_labels, 
			use_round_legend_box = dict_parameters["use_round_legend_box"], 
			legend_at_which_figure_corner = dict_parameters["legend_at_which_figure_corner"],
			legend_anchor_coordinate = legend_anchor_coordinate,
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