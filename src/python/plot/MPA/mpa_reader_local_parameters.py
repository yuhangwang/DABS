"""
MPA LOCAL PARAMETER READER
AUTHOR: YUHANG WANG 
DATE: 06-25-2015
"""
#--------------------------------------------------------
from mpa_syntax_marker  import ParameterSeparators as MpaParameterSeparators
from mpa_parameter_file import LocalParameters     as MpaLocalParameters
#--------------------------------------------------------

def read(list_parameters):
	"""
	Read local plot parameters 
	:param list_parameters: a list/tuple of parameters 
	:return: a python dictionary of dictionaries 
	"""
	dict_local_parametes = dict()
	dict_parameter_separators = MpaParameterSeparators.get_dict()
	dict_convention = MpaLocalParameters.get_convention()
	dict_defaults   = MpaLocalParameters.get_defaults()

	symbol_parameter_separator = dict_parameter_separators["PARAMETER SEPARATOR"]
	symbol_key_value_separator = dict_parameter_separators["KEY VALUE SEPARATOR"]

	for line in list_parameters:
		local_list = line.split(symbol_parameter_separator)
		local_dict = dict()
		for _item in local_list:
			key,value = _item.split(symbol_key_value_separator)
			key = key.strip()
			value = value.strip()
			local_dict[key] = value

		panle_indices = local_dict["PANEL INDICES"]
		dict_local_parametes[panle_indices] = dict()
		
		# [1] set the defaults
		for key,value in dict_defaults.items():
			dict_local_parametes[panle_indices][key] = value 
		
		# [2] update
		for key,value in local_dict.items():
			if key in dict_convention.keys():
				internal_key = dict_convention[key]
			else:
				print("WARNING: you have specified an unknown parameter: \"{0}\"".format(key))
				continue
			dict_local_parametes[panle_indices][internal_key] = value 

	return dict_local_parametes