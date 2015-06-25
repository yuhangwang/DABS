"""
MPA EXTERNAL DEPENDENCY PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""

class ExternalDependencyParameters:
	"""
	External dependency parameters
	"""
	_convention_ = {
		"USE LATEX":"use_latex",
		"USE SCIPY":"use_scipy",
		}

	_defaults_ = {
		"use_latex":False,
		"use_scipy":False,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return ExternalDependencyParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return ExternalDependencyParameters._defaults_.copy()

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "EXERNAL DEPENDENCY PARAMETERS"