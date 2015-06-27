"""
MPA PLOT PROXY: PANEL PROPERTY MODIFIER 
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""
#----------------------------------------------
import matplotlib.pyplot 
#----------------------------------------------
import mpa_modifier_panel   as MpaModifierPanel
#----------------------------------------------

def add_figure_panel_labels(object_axis, dict_plot_parameters):
	"""
	Proxy for adding figure panel labels 
	:param object object_axis: matplotlib Axis object 
	:param dict dict_plot_parameters: python dictionary of plotting parameters 

	"""
	object_old_axis_object = matplotlib.pyplot.gca() # store the current axis object
	if dict_plot_parameters["panel_label"] is not None:
		[x, y] = dict_plot_parameters["panel_label_box_anchor_coordinate"]
	 	MpaModifierPanel.add_panel_label(object_axis, x, y, 
	 		dict_plot_parameters["panel_label"],
			dict_plot_parameters["panel_label_font_size"],
			dict_plot_parameters["panel_label_horizontal_alignment"],
			dict_plot_parameters["panel_label_vertical_alignment"],
			dict_plot_parameters["panel_label_box_face_color"],
			dict_plot_parameters["panel_label_box_edge_color"],
			dict_plot_parameters["panel_label_box_opacity"],
			dict_plot_parameters["panel_label_box_padding"],
			dict_plot_parameters["panel_label_box_line_width"],
			dict_plot_parameters["panel_label_box_line_style"],
			dict_plot_parameters["panel_label_box_shape"],
			)
	# reset current active axis
	matplotlib.pyplot.sca(object_old_axis_object)