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
		"X LIMIT USER DEFINED ON":"x_limit_user_defined_on",
		"Y LIMIT USER DEFINED ON":"y_limit_user_defined_on",
		"X LIMIT TIGHT ON":"x_limit_tight_on",
		"Y LIMIT TIGHT ON":"y_limit_tight_on",
		"X MIN":"x_min",
		"X MAX":"x_max",
		"Y MIN":"y_min",
		"Y MAX":"y_max",
		"AXIS SPINE LIST":"axis_spine_list",
		"AXIS SPINE COLOR LIST":"axis_spine_color_list",
	}

	_default_ = {
		"x_label":'X',
		"y_label":'Y',
		"x_label_padding":None,
		"y_label_padding":None,
		"x_label_font_size":40,
		"y_label_font_size":40,
		"x_limit_user_defined_on":False,
		"y_limit_user_defined_on":False,
		"x_limit_tight_on":False,
		"y_limit_tight_on":False,
		"x_min":None,
		"x_max":None,
		"y_min":None,
		"y_max":None,
		"axis_spine_list":None,
		"axis_spine_color_list":None,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return AxisParameters._convention_

	@staticmethod
	def get_default():
		"""
		Get the default value dictionary
		"""
		return AxisParameters._default_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "AXIS PARAMETERS"