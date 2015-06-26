"""
MPA CORE: IO
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#----------------------------------------------------
# Import parameters
#----------------------------------------------------
from mpa_reader_input import read_input_information as input_reader
from mpa_reader_plot_parameters import read_plot_parameters as parameter_reader
from mpa_writer_figure import write_figure as figure_writer
#----------------------------------------------------


#----------------------------------------------------
#                     INPUT
#----------------------------------------------------
def read_config(file_configuration):
	"""
	Read a file containing a list of plot parameters 
	and put them into a python dictionary.
	:param str file_configuration: name of the input configuration file
	:return: (dict_global_parameters, dict_local_parameters, dict_file_parameters)
	"""
	print("======================================================")
	print("  Reading input configuration file")
	print("  File: {0}".format(file_configuration))
	print("======================================================")
	
	list_lines_file_parameters 	 = []
	list_lines_global_parameters = []
	list_lines_local_parameters  = []
    # Update parameters based on user's specifications
	with open(file_configuration, 'r') as IN:
		for line in IN:
			line = line.strip()
			if re.match(r"^@.+", line): 
				# file parameters
				line = line[1:].strip() 
				list_lines_file_parameters.append(line)

			elif re.match(r"^@@.+", line): 
				# global parameters
				line = line[2:].strip()
				list_lines_global_parameters.append(line)

			elif re.match(r"^@@@.+", line):
				# local parameters
				line = line[3:].strip()
				list_lines_local_parameters.append(line)
				
			else: continue # skip comments

#----------------------------------------------------
#                     OUTPUT
#----------------------------------------------------
def write_figure(*arg, **kwargs):
	"""
	Proxy for figure image writer
	"""
	return figure_writer(*arg, **kwargs)