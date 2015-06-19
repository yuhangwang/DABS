"""
Parameter conventions and defaults for PlotLine.py
Author: Yuhang Wang
Date: 06/19/2015
"""

class FigureParameters:
	"""
	Figure parameters
	"""
	_convention_ = {
		"FIGURE TITLE":"figure_title",
		"FIGURE TITLE FONT SIZE":"figure_title_font_size",
		"FIGURE LENGTH":"figure_length",
		"FIGURE HEIGHT":"figure_height",
		}

	_defaults_ = {
		"figure_title":None,
		"figure_title_font_size":40,
		"figure_length":12,
		"figure_height":8,
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


class AxisParameters:
	"""
	Axis parameters 
	"""		
	_convention_ = {
		"X LABEL":"xLabel",
		"Y LABEL":"yLabel",
		"X LABEL FONT SIZE":"xLabel_fontSize",
		"Y LABEL FONT SIZE":"yLabel_fontSize",
	}

	_defaults_ = {
		"xLabel":'X',
		"yLabel":'Y',
		"xLabel_fontSize":30,
		"yLabel_fontSize":30,
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


class LegendParameters:
	"""
	Legend parameters
	"""
	_convention_ = {
		"LEGEND LOCATION":"legend_location",
		"LEGEND BOX ANCHOR COORDINATE TUPLE":"lengend_box_anchor_coordiante_tuple",
		"LEGEND FRAME ALPHA":"lengend_frame_alpha",
		"LEGEND FONT SIZE":"legend_font_size",
		"ROUND LEGEND BOX":"use_round_legend_box",
		"SHOW LEGEND FRAME":"show_legend_frame",
		"NUMBER OF LEGEND COLUMNS":"number_of_legend_columns",
		}

	_defaults_ = {
		"legend_location":"lower left",
		"lengend_box_anchor_coordiante_tuple":(0.8, 0.1),
		"legend_frame_alpha":1.0,
		"use_round_legend_box":True,
		"show_legend_frame":True,
		"number_of_legend_columns":1,
		"legend_font_size":15,
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


class LineParameters:
	"""
	Line parameters 
	"""
	_convention_ = {
		"LINE STYLE":"lineStyle",
		}

	_defaults_ = {
		"lineStyle":'-',
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


class GridParameters:
	"""
	Grid parameters 
	"""
	_convention_ = {
		"GRID TICKS":"grid_ticks",
		"GRID AXIS":"grid_axis",
		"GRID LINE COLOR":"grid_line_color",
		"GRID LINE ALPHA":"grid_line_alpha",
		"GRID LINE WIDTH":"grid_line_width",
		"GRID LINE STYLE":"grid_line_style",
		"GRID Z ORDER":"grid_z_order",
		"SHOW GRID":"show_grid",
		}

	_defaults_ = {
		"grid_ticks":"major",
		"grid_axis":"both",
		"grid_line_color":'k',
		"grid_line_alpha":0.2,
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


class PlotParameters:
	"""
	Plot parameters
	"""
	def __init__(self):
		self._list_of_parameter_classes_ = [
			FigureParameters,
			AxisParameters,
			LineParameters,
			LegendParameters,
			GridParameters]

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