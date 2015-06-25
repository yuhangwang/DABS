"""
MPA CORE: PARAMETERS 
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#----------------------------------------------------
# Import parameters
#----------------------------------------------------
from mpa_parameter_axis  import AxisParameters
from mpa_parameter_color import ColorParameters
from mpa_parameter_dependency import ExternalDependencyParameters
from mpa_parameter_figure import FigureParameters
from mpa_parameter_grid   import GridParameters
from mpa_parameter_input  import InputFileParameters 
from mpa_parameter_legend import LegendParameters
from mpa_parameter_line   import LineParameters
from mpa_parameter_panel  import PanelParameters
from mpa_parameter_tick   import TickParameters
#----------------------------------------------------

class AllParameters:
	"""
	Plot parameters
	"""
	def __init__(self):
		self._list_of_parameter_classes_ = [
			ExternalDependencyParameters,
			FigureParameters,
			PanelParameters,
			AxisParameters,
			LineParameters,
			LegendParameters,
			GridParameters,
			TickParameters,
			ColorParameters,
			]

		self._convention_ = {}
		self._defaults_ = {}

		# Fill up self._convention_ and self._defaults_
		for _class in self._list_of_parameter_classes_:
			dict_convention = getattr(_class, "get_convention")()
			dict_defaults   = getattr(_class, "get_defaults")()
			for key, value in dict_convention.items():
				self._convention_[key] = value

			for key, value in dict_defaults.items():
				self._defaults_[key] = value


	def get_convention(self):
		return self._convention_

	def get_defaults(self):
		return self._defaults_.copy()


class ParameterManager:
	_list_of_parameter_classes_ =  [
			InputFileParameters,
			ExternalDependencyParameters,
			FigureParameters,
			PanelParameters,
			AxisParameters,
			LineParameters,
			LegendParameters,
			GridParameters,
			TickParameters,
			ColorParameters,
			]
	@staticmethod
	def show_parameters(parameter_type="public", file_output=None):
		msg = ""
		for _class in ParameterManager._list_of_parameter_classes_:
			dict_convention = getattr(_class, "get_convention")()
			dict_defaults   = getattr(_class, "get_defaults")()
			type_parameter = getattr(_class, "get_description")()
			msg += "------------------------------------------------\n"
			msg += "--------    {0} -------\n".format(type_parameter)
			msg += "------------------------------------------------\n"
			for key_public in sorted(dict_convention.keys()):
				key_internal = dict_convention[key_public]
				default_value = dict_defaults[key_internal]
				if parameter_type == "public":
					key = key_public
				else:
					key = key_internal
				msg += "{0}: {1}\n".format(key, default_value)
			msg += '\n'

		if file_output is not None:
			OUT = open(file_output, 'w')
			OUT.write(msg)
			OUT.close()
		else:
			print(msg)


if __name__ == "__main__":
	file_public = "PUBLIC_PARAMETERS.txt"
	file_internal = "INTERNAL_PARAMETERS.txt"
	manager = ParameterManager()
	manager.show_parameters("public", file_public)
	manager.show_parameters("internal", file_internal)