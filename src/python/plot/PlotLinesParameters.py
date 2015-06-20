"""
Parameter conventions and defaults for PlotLine.py
Author: Yuhang Wang
Date: 06/19/2015
"""

class ExternalDependencyParameters:
	"""
	External dependency parameters
	"""
	_convention_ = {
		"USE LATEX":"use_latex",
		"USE SCIPY":"use_scipy",
		}

	_defaults_ = {
		"use_latex":False,
		"use_scipy":False,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return ExternalDependencyParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return ExternalDependencyParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "EXERNAL DEPENDENCY PARAMETERS"


class FigureParameters:
	"""
	Figure parameters
	"""
	_convention_ = {
		"FIGURE TITLE":"figure_title",
		"FIGURE TITLE FONT SIZE":"figure_title_font_size",
		"FIGURE LENGTH":"figure_length",
		"FIGURE HEIGHT":"figure_height",
		"FIGURE NUMBER OF ROWS":"figure_number_of_rows",
		"FIGURE NUMBER OF COLUMNS":"figure_number_of_columns",
		"FIGURE SHARE X":"figure_share_x",
		"FIGURE SHARE Y":"figure_share_y",
		"FIGURE SUBPLOTS VERTICAL SPACING":"figure_subplots_vertical_spacing",
		"FIGURE_SUBPLOTS HORIZONTAL SPACING":"figure_subplots_horizontal_spacing",
		}

	_defaults_ = {
		"figure_title":None,
		"figure_title_font_size":40,
		"figure_length":12,
		"figure_height":8,
		"figure_number_of_rows":1,
		"figure_number_of_columns":1,
		"figure_share_x":False,
		"figure_share_y":False,
		"figure_subplots_vertical_spacing":0,
		"figure_subplots_horizontal_spacing":0,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return FigureParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return FigureParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "FIGURE PARAMETERS"


class AxisParameters:
	"""
	Axis parameters 
	"""		
	_convention_ = {
		"X LABEL":"x_label",
		"Y LABEL":"y_label",
		"X LABEL PADDING":"x_label_padding",
		"Y LABEL PADDING":"y_label_padding",
		"X LABEL FONT SIZE":"x_label_font_size",
		"Y LABEL FONT SIZE":"y_label_font_size",
	}

	_defaults_ = {
		"x_label":'X',
		"y_label":'Y',
		"x_label_padding":None,
		"y_label_padding":None,
		"x_label_font_size":30,
		"y_label_font_size":30,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return AxisParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return AxisParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "AXIS PARAMETERS"

class LegendParameters:
	"""
	Legend parameters
	"""
	_convention_ = {
		"LEGEND LOCATION":"legend_location",
		"LEGEND BOX ANCHOR COORDINATE TUPLE":"legend_box_anchor_coordinate_tuple",
		"LEGEND FRAME TRANSPARENCY":"legend_frame_transparency",
		"LEGEND FONT SIZE":"legend_font_size",
		"LEGEND FONT WEIGHT":"legend_font_weight",
		"LEGEND LINE WIDTH":"legend_line_width",
		"LEGEND MARKER SCALE":"legend_marker_scale",
		"LEGEND NUMBER OF MAKRER POINTS":"legend_number_of_marker_points",
		"LEGEND NUMBER OF SCATTER MAKRER POINTS":"legend_number_of_scatter_marker_points",
		"LEGEND HANDLE LENGTH":"legend_handle_length",
		"LEGEND BORDER PADDING":"legend_border_padding",
		"LEGEND VERTICAL SPACING":"legend_vertical_spacing",
		"LEGEND PADDING BETWEEN HANDLE AND TEXT":"legend_padding_between_handle_and_text",
		"LEGEND PADDING BETWEEN BORDER AND AXES":"legend_padding_between_border_and_axes",
		"LEGEND COLUMN SPACING":"legend_column_spacing",
		"LEGEND FACE COLOR":"legend_face_color",
		"LEGEND EDGE COLOR":"legend_edge_color",
		"LEGEND FACE TRANSPARENCY":"legend_face_transparency",
		"ROUND LEGEND BOX":"use_round_legend_box",
		"SHOW LEGEND FRAME":"show_legend_frame",
		"NUMBER OF LEGEND COLUMNS":"number_of_legend_columns",
		}

	_defaults_ = {
		"legend_location":"lower left",
		"legend_box_anchor_coordinate_tuple":(0.8, 0.1),
		"legend_frame_transparency":0.5,
		"legend_font_size":15,
		"legend_font_weight":800,
		"legend_line_width":8,
		"legend_marker_scale":1,
		"legend_number_of_marker_points":None,
		"legend_number_of_scatter_marker_points":None,
		"legend_handle_length":2,
		"legend_border_padding":0.5,
		"legend_vertical_spacing":0.5,
		"legend_padding_between_handle_and_text":0.5,
		"legend_padding_between_border_and_axes":0,
		"legend_column_spacing":0.8,
		"legend_face_color":'w',
		"legend_edge_color":'k',
		"legend_face_transparency":1.0,
		"use_round_legend_box":True,
		"show_legend_frame":True,
		"number_of_legend_columns":1,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return LegendParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return LegendParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "LEGEND PARAMETERS"

class ColorParameters:
	"""
	Color parameters 
	"""
	_convention_ = {
		"COLOR ORDER":"color_order",
		}

	_defaults_ = {
		"color_order":['k','r','g','b','m','y','c'],
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return ColorParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return ColorParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "COLOR PARAMETERS"


class LineParameters:
	"""
	Line parameters 
	"""
	_convention_ = {
		"LINE STYLE":"line_style",
		"LINE TRANSPARENCY":"line_transparency",
		"SHOW BLOCK AVERAGED LINE":"show_block_averaged_line",
		"LINE BLOCK AVERAGE BLOCK SIZE":"line_block_average_block_size",
		"BLOCK AVERAGED LINE WIDTH":"block_averaged_line_width",
		}

	_defaults_ = {
		"line_style":'-',
		"line_transparency":1.0,
		"show_block_averaged_line":False,
		"line_block_average_block_size":1,
		"block_averaged_line_width":2,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return LineParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return LineParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "LINE PARAMETERS"


class GridParameters:
	"""
	Grid parameters 
	"""
	_convention_ = {
		"GRID TICKS":"grid_ticks",
		"GRID AXIS":"grid_axis",
		"GRID LINE COLOR":"grid_line_color",
		"GRID LINE TRANSPARENCY":"grid_line_transparency",
		"GRID LINE WIDTH":"grid_line_width",
		"GRID LINE STYLE":"grid_line_style",
		"GRID Z ORDER":"grid_z_order",
		"SHOW GRID":"show_grid",
		}

	_defaults_ = {
		"grid_ticks":"major",
		"grid_axis":"both",
		"grid_line_color":'k',
		"grid_line_transparency":0.2,
		"grid_line_width":1,
		"grid_line_style":'--',
		"grid_z_order":-1,
		"show_grid":True,
		}

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return GridParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return GridParameters._defaults_

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "GRID PARAMETERS"


class TickParameters:
	"""
	Tick and its label parameters
	"""
	_convention_ = {
		"X TICK MAJOR MINOR OR BOTH":"x_tick_major_minor_or_both",
		"Y TICK MAJOR MINOR OR BOTH":"y_tick_major_minor_or_both",
		"X TICK IN OUT OR INOUT":"x_tick_in_out_or_inout",
		"Y TICK IN OUT OR INOUT":"y_tick_in_out_or_inout",
		"X TICK LENGTH":"x_tick_length",
		"Y TICK LENGTH":"y_tick_length",
		"X TICK WIDTH":"x_tick_width",
		"Y TICK WIDTH":"y_tick_width",
		"X TICK LABEL FONT SIZE":"x_tick_label_font_size",
		"Y TICK LABEL FONT SIZE":"y_tick_label_font_size",
		"X TICK LABEL FONT WEIGHT":"x_tick_label_font_weight",
		"Y TICK LABEL FONT WEIGHT":"y_tick_label_font_weight",
		"X TICK COLOR":"x_tick_color",
		"Y TICK COLOR":"y_tick_color",
		"X TICK LABEL COLOR":"x_tick_label_color",
		"Y TICK LABEL COLOR":"y_tick_label_color",
		"X TICK LABEL PADDING":"x_tick_label_padding",
		"Y TICK LABEL PADDING":"y_tick_label_padding",
		"X TICK AND LABEL Z ORDER":"x_tick_and_label_z_order",
		"Y TICK AND LABEL Z ORDER":"y_tick_and_label_z_order",
		"X TICK SHOW TOP":"x_tick_show_top",
		"X TICK SHOW BOTTOM":"x_tick_show_bottom",
		"Y TICK SHOW LEFT":"y_tick_show_left",
		"Y TICK SHOW RIGHT":"y_tick_show_right",		
		"X TICK LABEL SHOW TOP":"x_tick_label_show_top",
		"X TICK LABEL SHOW BOTTOM":"x_tick_label_show_bottom",
		"Y TICK LABEL SHOW LEFT":"y_tick_label_show_left",
		"Y TICK LABEL SHOW RIGHT":"y_tick_label_show_right",
		"X TICK LABEL NUMBER OF DECIMAL PLACES":"x_tick_label_number_of_decimal_places",
		"Y TICK LABEL NUMBER OF DECIMAL PLACES":"y_tick_label_number_of_decimal_places",
		"X TICK RESET OLD PARAMETER":"x_tick_reset_old_parameter",
		"Y TICK RESET OLD PARAMETER":"y_tick_reset_old_parameter",
		"HIDE OVERLAPPING X TICK LABEL":"x_tick_label_hide_overlap",
		"HIDE OVERLAPPING Y TICK LABEL":"y_tick_label_hide_overlap",
		"X TICK MAX NUMBER":"x_tick_max_number",
		"Y TICK MAX NUMBER":"y_tick_max_number",
		}

	# Default parameters corresponding to entries in _convention_
	_user_defaults_ = {
		"x_tick_major_minor_or_both":"major",
		"y_tick_major_minor_or_both":"major",
		"x_tick_in_out_or_inout":"inout",
		"y_tick_in_out_or_inout":"inout",
		"x_tick_length":5,
		"y_tick_length":5,
		"x_tick_width":2,
		"y_tick_width":2,
		"x_tick_label_font_size":20,
		"y_tick_label_font_size":20,
		"x_tick_label_font_weight":0,
		"y_tick_label_font_weight":0,
		"x_tick_color":'k',
		"y_tick_color":'k',
		"x_tick_label_color":'k',
		"y_tick_label_color":'k',
		"x_tick_label_padding":10,
		"y_tick_label_padding":10,
		"x_tick_and_label_z_order":0,
		"y_tick_and_label_z_order":0,
		"x_tick_show_top":True,
		"x_tick_show_bottom":True,
		"y_tick_show_left":True,
		"y_tick_show_right":True,
		"x_tick_label_show_top":False,
		"x_tick_label_show_bottom":True,
		"y_tick_label_show_left":True,
		"y_tick_label_show_right":False,
		"x_tick_label_number_of_decimal_places":None,
		"y_tick_label_number_of_decimal_places":None,
		"x_tick_reset_old_parameter":False,
		"y_tick_reset_old_parameter":False,
		"x_tick_label_hide_overlap":False,
		"y_tick_label_hide_overlap":False,
		"x_tick_max_number":10,
		"y_tick_max_number":10,
		}

	# The following additional defaults are only used internally
	# for the sake of symmetry between x and y parameters.
	# However they are not exposed to users, because
	# these parameters are meaningless.
	# For example, 'y' axis doesn't have ticks on the top.
	# This is useful since we can now use a for loop
	# to iterate all options for x and y axis uniformly.
	_internal_defaults_ = {
		"y_tick_show_top":False,
		"y_tick_show_bottom":False,
		"x_tick_show_left":False,
		"x_tick_show_right":False,
		"y_tick_label_show_top":False,
		"y_tick_label_show_bottom":False,
		"x_tick_label_show_left":False,
		"x_tick_label_show_right":False,
		}

	## Now merge the two default dictionaries
	_defaults_ = _user_defaults_.copy()
	_defaults_.update(_internal_defaults_)

	@staticmethod
	def get_convention():
		"""
		Get the convention dictionary
		"""
		return TickParameters._convention_

	@staticmethod
	def get_defaults():
		"""
		Get the default value dictionary
		"""
		return TickParameters._defaults_	

	@staticmethod
	def get_description():
		"""
		Description of this class 
		"""
		return "TICK PARAMETERS"


class PlotParameters:
	"""
	Plot parameters
	"""
	def __init__(self):
		self._list_of_parameter_classes_ = [
			ExternalDependencyParameters,
			FigureParameters,
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
		return self._defaults_