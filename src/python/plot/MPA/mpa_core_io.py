"""
MPA CORE: IO
AUTHOR: YUHANG WANG 
DATE: 06-24-2015
"""
#----------------------------------------------------
# Import parameters
#----------------------------------------------------
import mpa_reader_file_parameters   as MpaFileParameterReader
import mpa_reader_global_parameters as MpaGlobalParameterReader
import mpa_reader_local_parameters  as MpaLocalParameterReader
impore mpa_writer_figure 			as MpaFigureWriter
#----------------------------------------------------


#----------------------------------------------------
#                     INPUT
#----------------------------------------------------
def read_config(file_configuration):
	"""
	Read a file containing a list of plot parameters 
	and put them into a python dictionary.
	:param str file_configuration: name of the input configuration file
	:return: (dict_file_parameters, dict_global_plot_parameters, dict_local_plot_parameters)
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

	# Read file parameters 
	dict_file_parameters = MpaFigureWriter.read(list_lines_file_parameters)

	# Read global parameters
	dict_global_plot_parameters = MpaGlobalParameterReader.read(list_lines_global_parameters)

	# Read local parameters 
	dict_local_plot_parameters = MpaLocalParameterReader.read(list_lines_local_parameters)

	return (dict_file_parameters, dict_global_plot_parameters, dict_local_plot_parameters)

#----------------------------------------------------
#                     OUTPUT
#----------------------------------------------------
def write_figure(*arg, **kwargs):
	"""
	Proxy for figure image writer
	"""
	return MpaFigureWriter.write(*arg, **kwargs)