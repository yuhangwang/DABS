"""
MPA PLOT PARAMETER READER 
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#--------------------------------------------------------
import mpa_toolkit as MPA_TOOL
#--------------------------------------------------------

def read_plot_parameters(file_plot_parameters, dict_convention, dict_default_parameters):
	"""
	Read a file containing a list of plot parameters 
	and put them into a python dictionary.
	:param str file_plot_parameters: name of the file that contains plotting parameters 
	:return: python dictionary
	"""
	print("======================================================")
	print("  Read plotting parameters")
	print("  File: {0}".format(file_plot_parameters))
	print("======================================================")
	
	# A dict for storing plot parameters
	dict_plot_parameters = dict()

	# copy default parameters
	for key, value in dict_default_parameters.items():
		dict_plot_parameters[key] = value 

    # Update parameters based on user's specifications
	with open(file_plot_parameters, 'r') as IN:
		for line in IN:
			line = line.strip()
			key,value = line.split(':')

			key = key.strip()
			value = value.strip()

			# Only record parameters defined in "dict_convention"
			# Otherwise skip the unknown parameters
			if key in dict_convention.keys():
				new_key = dict_convention[key]
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

			print("{0}\t==>\t{1}".format(new_key, value))
			dict_plot_parameters[new_key] = value
	print("\n")
	return dict_plot_parameters