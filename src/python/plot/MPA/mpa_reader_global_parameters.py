"""
MPA PLOT PARAMETER READER 
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#--------------------------------------------------------
import mpa_toolkit as MPA_TOOL
from mpa_syntax_marker  import ParameterSeparators as MpaParameterSeparators
from mpa_parameter_file import GlobalParameters      as MpaGlobalParameters
#--------------------------------------------------------

def read(list_parameters):
	"""
	Read global plot parameters
	:param list_parameters: a list/tuple of parameters  
	:return: a python dictionary 
	"""
	dict_global_parametes = dict()
	dict_parameter_separators = MpaParameterSeparators.get_dict()
	dict_convention = MpaGlobalParameters.get_convention()
	dict_defaults = MpaGlobalParameters.get_defaults()

	symbol_parameter_separator = dict_parameter_separators["PARAMETER SEPARATOR"]
	symbol_key_value_separator = dict_parameter_separators["KEY VALUE SEPARATOR"]

	for line in list_parameters:
		local_list = line.split(symbol_parameter_separator)
		local_dict = dict()
		for _item in local_list:
			key,value = _item.split(symbol_key_value_separator)
			key = key.strip()
			value = value.strip()

			# convert to 'raw string literal' to preserve LaTex formating
			value = r"{0}".format(value)

			# check whether string "value" can be converted to boolean
			value = MPA_TOOL.string_to_bool_or_not(value)

			# If not, try to convert it to a number
			value = MPA_TOOL.string_to_number_or_not(value)

			# Try to convert it to a list
			if type(value) is str and MPA_TOOL.is_convertible_to_list(value):
				value = MPA_TOOL.string_to_tuple_or_not(value)

			local_dict[key] = value

		# [1] set the defaults
		for key,value in dict_defaults.items():
			dict_global_parametes[file_name][key] = value 

		# [2] update
		for key,value in local_dict.items():
			if key in dict_convention.keys():
				internal_key = dict_convention[key]
			else:
				print("WARNING: you have specified an unknown parameter: \"{0}\"".format(key))
				continue
			dict_global_parametes[internal_key] = value 

	return dict_plot_parameter_global