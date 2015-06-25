"""
MPA PLOT PROXY: PANEL LABEL
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#----------------------------------------------
import matplotlib.pyplot 
#----------------------------------------------
import mpa_modifier_axis   as MpaModifierAxis 
#----------------------------------------------

def add_figure_panel_labels(dict_panel_information, dict_plot_parameters):
	"""
	Proxy for adding figure panel labels 
	:param dict_panel_information: a dictionary of dictionaries. 
		The key is the panel ID (i.e., 0, 1, 2, ...);
		The value is a sub-dictionary with keys: "object_axis", "list_line_objects", "list_legend_labels", "legend_anchor_coordinate"
	:param dict dict_plot_parameters: python dictionary of plotting parameters 

	"""
	object_old_axis_object = matplotlib.pyplot.gca() # store the current axis object
	for _panel_index_tuple, _dict_panel in dict_panel_information.items():
		object_axis = _dict_panel["object_axis"]
		panel_label = _dict_panel["panel_label"]
		[x, y] = _dict_panel["panel_label_coordinate"]
		if panel_label is not None:
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