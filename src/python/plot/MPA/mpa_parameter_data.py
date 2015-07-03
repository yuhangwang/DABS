"""
MPA DATA PARAMETERS
AUTHOR: YUHANG WANG
DATE: 06-26-2015
"""


class DataParameters:
	"""
	Input data parameters 
	"""
	_convention_ = {
		"DATA FILE":"data_file",
		"DATA VALUE":"data_value",
		"DATA LEGEND":"data_legend",
		"DATA LEGEND ON":"data_legend_on",
		"DATA LEGEND PANEL INDICES":"data_legend_panel_indices",
		'DATA PANEL INDICES':"data_panel_indices",
		"DATA LINE STYLE":"data_line_style",
		"DATA LINE COLOR":"data_line_color",
		"DATA LINE OPACITY":"data_line_opacity",
		"DATA SHOW BLOCK AVERAGE":"data_show_block_average",
		"DATA BLOCK AVERAGE BLOCK SIZE":"data_block_average_block_size",
		"DATA BLOCK AVERAGE LINE WIDTH":"data_block_average_line_width",
		"DATA PLOT TYPE":"data_plot_type",
		"DATA MATRIX TRANSPOSE":"data_matrix_transpose",
		"DATA MATRIX COLOR BAR ON":"data_matrix_color_bar_on",
		"DATA MATRIX COLOR BAR PANEL INDICES":"data_matrix_color_bar_panel_indices",
		}

	_default_ = {
		"data_file":None,
		"data_value":None,
		"data_legend":None,
		"data_legend_on":False,
		"data_legend_panel_indices": (0,0),
		"data_panel_indices":(0,0),
		"data_line_style":'-',
		"data_line_color":None,
		"data_line_opacity":1.0,
		"data_show_block_average":False,
		"data_block_average_block_size":1,
		"data_block_average_line_width":1,
		"data_plot_type":"line",
		"data_matrix_transpose":False,
		"data_matrix_color_bar_on":False,
		"data_matrix_color_bar_panel_indices":(0,0),
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return DataParameters._convention_

	@staticmethod
	def get_default():
		"""
		Get the default value dictionary
		"""
		return DataParameters._default_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "INPUT DATA FILE KEYWORDS"
