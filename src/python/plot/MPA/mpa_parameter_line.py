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

		}

	_default_ = {

		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return LineParameters._convention_

	@staticmethod
	def get_default():
		"""
		Get the default value dictionary
		"""
		return LineParameters._default_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "LINE PARAMETERS"
