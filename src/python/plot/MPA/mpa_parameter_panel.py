"""
MPA FIGURE PANEL PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""


class PanelParameters:
	"""
	Panel Parameters
	"""
	_convention_ = {
		"PANEL LABEL FONT SIZE":"panel_label_font_size",
		"PANEL LABEL HORIZONTAL ALIGNMENT":"panel_label_horizontal_alignment",
		"PANEL LABEL VERTICAL ALIGNMENT":"panel_label_vertical_alignment",
		"PANEL BOX FACE COLOR":"panel_box_face_color",
		"PANEL BOX EDGE COLOR":"panel_box_edge_color",
		"PANEL BOX OPACITY":"panel_box_opacity",
		"PANEL BOX PADDING":"panel_box_padding",
		"PANEL BOX LINE WIDTH":"panel_box_line_width",
		"PANEL BOX LINE STYLE":"panel_box_line_style",
		"PANEL BOX SHAPE":"panel_box_shape",
		}

	_defaults_ = {
		"panel_label_font_size":25,
		"panel_label_horizontal_alignment":"left",
		"panel_label_vertical_alignment":"center",
		"panel_box_face_color":'w',
		"panel_box_edge_color":'w',
		"panel_box_opacity":0.8,
		"panel_box_padding":0.2,
		"panel_box_line_width":1,
		"panel_box_line_style":"solid",
		"panel_box_shape":"square",
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return PanelParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return PanelParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "PANEL PARAMETERS"