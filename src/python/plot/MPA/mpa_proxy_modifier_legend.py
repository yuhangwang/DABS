"""
MPA PROXY: LEGEND MODIFIER
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#---------------------------------------------------
import matplotlib.pyplot
#---------------------------------------------------
import mpa_modifier_legend as MpaModifierLegend 
#---------------------------------------------------


def refine_legend(dict_panel_information,dict_plot_parameters):
	"""
	Add and refine the legends
	:param dict_panel_information: a dictionary of information for all figure panels indexed by panel index tuple
	:param dict dict_plot_parameters: python dictionary of plotting parameters 
	"""
	object_old_axis_object = matplotlib.pyplot.gca() # store the current axis object
	for _panel_indices, _dict_panel in dict_panel_information.items():
		object_axis = _dict_panel["object_axis"]
		list_line_objects = _dict_panel["list_line_objects"]
		list_legend_labels = _dict_panel["list_legend_labels"]
		legend_anchor_coordinate = _dict_panel["legend_anchor_coordinate"]
		legend_number_of_columns = _dict_panel["legend_number_of_columns"]

		# set new current axis
		matplotlib.pyplot.sca(object_axis)
		
		MpaModifierLegend.add_legend(list_line_objects, list_legend_labels, 
			use_round_legend_box = dict_plot_parameters["use_round_legend_box"], 
			legend_anchor_corner = dict_plot_parameters["legend_anchor_corner"],
			legend_anchor_coordinate = legend_anchor_coordinate,
			show_legend_frame = dict_plot_parameters["show_legend_frame"],
			legend_frame_opacity = dict_plot_parameters["legend_frame_opacity"],
			legend_number_of_columns = legend_number_of_columns,
			legend_font_size = dict_plot_parameters["legend_font_size"],
			legend_font_weight = dict_plot_parameters["legend_font_weight"],
			legend_line_width = dict_plot_parameters["legend_line_width"],
			legend_marker_scale = dict_plot_parameters["legend_marker_scale"],
			legend_number_of_marker_points = dict_plot_parameters["legend_number_of_marker_points"],
			legend_number_of_scatter_marker_points = dict_plot_parameters["legend_number_of_marker_points"],
			legend_handle_length = dict_plot_parameters["legend_handle_length"],
			legend_border_padding = dict_plot_parameters["legend_border_padding"],
			legend_vertical_spacing = dict_plot_parameters["legend_vertical_spacing"],
			legend_padding_between_handle_and_text = dict_plot_parameters["legend_padding_between_handle_and_text"],
			legend_padding_between_border_and_axes = dict_plot_parameters["legend_padding_between_border_and_axes"],
			legend_column_spacing = dict_plot_parameters["legend_column_spacing"],
			legend_face_color = dict_plot_parameters["legend_face_color"],
			legend_edge_color = dict_plot_parameters["legend_edge_color"],
			)
	
	# reset current axis back to the original
	matplotlib.pyplot.sca(object_old_axis_object)