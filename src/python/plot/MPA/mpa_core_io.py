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
def read_input(*arg, **kwargs):
	"""
	Proxy for user input file information reader
	"""
	return input_reader(*arg, **kwargs)

def read_parameter(*arg, **kwargs):
	"""
	Proxy for plot parameter reader
	"""
	return parameter_reader(*arg, **kwargs)

#----------------------------------------------------
#                     OUTPUT
#----------------------------------------------------
def write_figure(*arg, **kwargs):
	"""
	Proxy for figure image writer
	"""
	return figure_writer(*arg, **kwargs)