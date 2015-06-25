"""
MPA LEGEND PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""

class LegendParameters:
	"""
	Legend parameters
	"""
	_convention_ = {
		"LEGEND ON":"legend_on",
		"LEGEND AT WHICH FIGURE CORNER":"legend_at_which_figure_corner",
		"LEGEND FRAME OPACITY":"legend_frame_opacity",
		"LEGEND FONT SIZE":"legend_font_size",
		"LEGEND FONT WEIGHT":"legend_font_weight",
		"LEGEND LINE WIDTH":"legend_line_width",
		"LEGEND MARKER SCALE":"legend_marker_scale",
		"LEGEND NUMBER OF MAKRER POINTS":"legend_number_of_marker_points",
		"LEGEND NUMBER OF SCATTER MAKRER POINTS":"legend_number_of_scatter_marker_points",
		"LEGEND HANDLE LENGTH":"legend_handle_length",
		"LEGEND BORDER PADDING":"legend_border_padding",
		"LEGEND VERTICAL SPACING":"legend_vertical_spacing",
		"LEGEND PADDING BETWEEN HANDLE AND TEXT":"legend_padding_between_handle_and_text",
		"LEGEND PADDING BETWEEN BORDER AND AXES":"legend_padding_between_border_and_axes",
		"LEGEND COLUMN SPACING":"legend_column_spacing",
		"LEGEND FACE COLOR":"legend_face_color",
		"LEGEND EDGE COLOR":"legend_edge_color",
		"LEGEND FACE OPACITY":"legend_face_opacity",
		"ROUND LEGEND BOX":"use_round_legend_box",
		"SHOW LEGEND FRAME":"show_legend_frame",
		"NUMBER OF LEGEND COLUMNS":"number_of_legend_columns",
		"USE GLOBAL LEGEND":"use_global_legend",
		}

	_defaults_ = {
		"legend_on":False,
		"legend_at_which_figure_corner":"lower left",
		"legend_frame_opacity":0.5,
		"legend_font_size":15,
		"legend_font_weight":800,
		"legend_line_width":8,
		"legend_marker_scale":1,
		"legend_number_of_marker_points":None,
		"legend_number_of_scatter_marker_points":None,
		"legend_handle_length":2,
		"legend_border_padding":0.5,
		"legend_vertical_spacing":0.5,
		"legend_padding_between_handle_and_text":0.5,
		"legend_padding_between_border_and_axes":0,
		"legend_column_spacing":0.8,
		"legend_face_color":'w',
		"legend_edge_color":'k',
		"legend_face_opacity":1.0,
		"use_round_legend_box":True,
		"show_legend_frame":True,
		"number_of_legend_columns":1,
		"use_global_legend":True,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return LegendParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return LegendParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "LEGEND PARAMETERS"