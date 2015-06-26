"""
MPA PARAMETER: CREATE TWIN AXIS
AUTHOR: YUHANG WANG
DATE: 06-25-2015
"""

class TwinAxisParameters:
	"""
	Parameters for creating twin axis 
	"""
	_convention_ = {
		"TWINX AXIS SOURCE INDEX LIST":"twinx_axis_source_index_list",
		"TWINY AXIS SOURCE INDEX LIST":"twiny_axis_source_index_list",
	}

	_defaults_ = {
		"twinx_axis_source_index_list":None,
		"twiny_axis_source_index_list":None,
	}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return TwinAxisParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return TwinAxisParameters._defaults_.copy()	

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "TWIN AXIS PARAMETERS"
