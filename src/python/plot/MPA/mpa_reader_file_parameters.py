"""
MPA INPUT INFORMATION READER
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#--------------------------------------------------------
import numpy
#--------------------------------------------------------
import mpa_toolkit as MPA_TOOL
#--------------------------------------------------------

def read(file_input_information, dict_default, dict_convention):
	"""
	Read file parameters 
	:param str file_input_information: file that contains a list of file names 
	:param dict dict_default: a dict that has all the default values
	:param dict dict_convention: a dictionary of input parameter keyword convention pairs
	:return: a python list of numpy arrays
	"""
	print("======================================================")
	print("  Read input data files and legends")
	print("  File: {0}".format(file_input_information))
	print("======================================================")
	
	list_input_information = []
	with open(file_input_information, 'r') as IN:
		for line in IN:
			line = line.strip()
			tmp_list = line.split(";")

			# remove extra leading/trailing white spaces
			for i in range(len(tmp_list)):
				tmp_list[i] = tmp_list[i].strip()

			# use default values
			dict_current_line = dict()
			for key,value in dict_default.items():
				dict_current_line[key] = value

			for item in tmp_list:
				key, value = item.split(":")
				key = key.strip()
				value = value.strip()
				
				# change to internal keyword
				if key in dict_convention.keys():
					key = dict_convention[key]
				else:
					msg = "ERROR HINT: input keyword not recognized: \"{0}\"".format(key)
					raise UserWarning(msg)

				# convert string to list/tuple
				if MPA_TOOL.is_convertible_to_list(value):
					value = MPA_TOOL.string_to_tuple_or_not(value)
				else:
					value = MPA_TOOL.string_to_bool_or_not(value)
					value = MPA_TOOL.string_to_number_or_not(value)

				# convert string "None" to real python None type
				value = MPA_TOOL.string_to_None_or_not(value)

				dict_current_line[key] = value

			# load input data
			dict_current_line["input_data"] = numpy.loadtxt(dict_current_line["file"])

			print("Loading data file: {0}".format(dict_current_line["file"]))

			# append
			list_input_information.append(dict_current_line)

	return list_input_information