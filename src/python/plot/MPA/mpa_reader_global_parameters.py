"""
MPA PLOT PARAMETER READER 
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#--------------------------------------------------------
import mpa_toolkit as MPA_TOOL
#--------------------------------------------------------

def read_global_parameters():
			key,value = line.split(':')

			key = key.strip()
			value = value.strip()

			# Only record parameters defined in "
			dict_convention_global
			# Otherwise skip the unknown parameters
			if key in 
			dict_convention_global.keys():
				new_key = 
				dict_convention_global[key]
			else:
				print("WARNING: you have specified an unknown parameter: \"{0}\"".format(key))
				continue

			# convert to 'raw string literal' to preserve LaTex formating
			value = r"{0}".format(value)

			# check whether string "value" can be converted to boolean
			value = MPA_TOOL.string_to_bool_or_not(value)

			# If not, try to convert it to a number
			value = MPA_TOOL.string_to_number_or_not(value)

			# if "new_key" is "color_order", then convert it a list
			if type(value) is str and MPA_TOOL.is_convertible_to_list(value):
				value = MPA_TOOL.string_to_tuple_or_not(value)

			dict_plot_parameter_global[new_key] = value
	return dict_plot_parameter_global