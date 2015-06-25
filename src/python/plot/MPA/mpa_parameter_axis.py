"""
MPA FIGURE AXIS PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""

class AxisParameters:
	"""
	Axis parameters 
	"""		
	_convention_ = {
		"X LABEL":"x_label",
		"Y LABEL":"y_label",
		"X LABEL PADDING":"x_label_padding",
		"Y LABEL PADDING":"y_label_padding",
		"X LABEL FONT SIZE":"x_label_font_size",
		"Y LABEL FONT SIZE":"y_label_font_size",
	}

	_defaults_ = {
		"x_label":'X',
		"y_label":'Y',
		"x_label_padding":None,
		"y_label_padding":None,
		"x_label_font_size":40,
		"y_label_font_size":40,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return AxisParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return AxisParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "AXIS PARAMETERS"