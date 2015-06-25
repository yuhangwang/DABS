"""
MPA COLOR PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""


class ColorParameters:
	"""
	Color parameters 
	"""
	_convention_ = {
		"COLOR ORDER":"color_order",
		"USE COLOR MAP COOL":"use_color_map_cool",
		}

	_defaults_ = {
		"color_order":['k','r','g','b','m','y','c'],
		"use_color_map_cool":False,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return ColorParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return ColorParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "COLOR PARAMETERS"
