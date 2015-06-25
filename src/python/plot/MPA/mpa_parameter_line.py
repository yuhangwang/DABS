"""
MPA LINE PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""


class LineParameters:
	"""
	Line parameters 
	"""
	_convention_ = {
		"LINE STYLE":"line_style",
		"LINE OPACITY":"line_opacity",
		"SHOW BLOCK AVERAGED LINE":"show_block_averaged_line",
		"BLOCK AVERAGED LINE WIDTH":"block_averaged_line_width",
		}

	_defaults_ = {
		"line_style":'-',
		"line_opacity":1.0,
		"show_block_averaged_line":False,
		"block_averaged_line_width":1,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return LineParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return LineParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "LINE PARAMETERS"
