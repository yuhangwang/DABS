"""
MPA INPUT PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""


class InputFileParameters:
	"""
	Input file parameters 
	"""
	_convention_ = {
		"FILE":"file",
		"LEGEND":"legend",
		"LEGEND ANCHOR COORDINATE":"legend_anchor_coordinate",
		"LEGEND PANEL INDICES":"legend_panel_indices",
		'PANEL INDICES':"panel_indices",
		"PANEL LABEL":"panel_label",
		"PANEL LABEL COORDINATE":"panel_label_coordinate",
		"X MIN":"x_min",
		"X MAX":"x_max",
		"Y MIN":"y_min",
		"Y MAX":"y_max",
		}

	_defaults_ = {
		"file":None,
		"legend":None,
		"legend_anchor_coordinate": (0.9,0.9),
		"legend_panel_indices": (0,0),
		"panel_indices":(0,0),
		"panel_label":None,
		"panel_label_coordinate":None,
		"x_min":None,
		"x_max":None,
		"y_min":None,
		"y_max":None,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return InputFileParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return InputFileParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "INPUT FILE KEYWORDS"
