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
		"PANEL INDICES":"panel_indices",
		"PANEL LABEL ON":"panel_label_on",
		"PANEL LABEL":"panel_label",
		"PANEL LABEL COORDINATE":"panel_label_coordinate",
		"PANEL LABEL FONT SIZE":"panel_label_font_size",
		"PANEL LABEL HORIZONTAL ALIGNMENT":"panel_label_horizontal_alignment",
		"PANEL LABEL VERTICAL ALIGNMENT":"panel_label_vertical_alignment",
		"PANEL LABEL BOX FACE COLOR":"panel_label_box_face_color",
		"PANEL LABEL BOX EDGE COLOR":"panel_label_box_edge_color",
		"PANEL LABEL BOX OPACITY":"panel_label_box_opacity",
		"PANEL LABEL BOX PADDING":"panel_label_box_padding",
		"PANEL LABEL BOX LINE WIDTH":"panel_label_box_line_width",
		"PANEL LABEL BOX LINE STYLE":"panel_label_box_line_style",
		"PANEL LABEL BOX SHAPE":"panel_label_box_shape",
		}

	_default_ = {
		"panel_indices":None,
		"panel_label_on":False,
		"panel_label":None,
		"panel_label_coordinate":None,
		"panel_label_font_size":25,
		"panel_label_horizontal_alignment":"left",
		"panel_label_vertical_alignment":"center",
		"panel_label_box_face_color":'w',
		"panel_label_box_edge_color":'w',
		"panel_label_box_opacity":0.8,
		"panel_label_box_padding":0.2,
		"panel_label_box_line_width":1,
		"panel_label_box_line_style":"solid",
		"panel_label_box_shape":"square",
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return PanelParameters._convention_

	@staticmethod
	def get_default():
		"""
		Get the default value dictionary
		"""
		return PanelParameters._default_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "PANEL PARAMETERS"