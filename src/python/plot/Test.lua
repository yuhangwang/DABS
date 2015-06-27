#!/Scr/scr-test-steven/local/bin/lua
----------------------------------------------------------
-- Tests for PlotLines.py
----------------------------------------------------------
-- Author: Yuhang Wang -----------------------------------
-- Date: 06/20/2015 --------------------------------------
----------------------------------------------------------

----------------------------------------------------------
-- Global flags
----------------------------------------------------------
ID_test_case = 1
FLAG_create_test_data = true
----------------------------------------------------------

MpaTk = require("mpa_toolkit_module")
dir_data_root = "./data"
dir_figure_root = "./figure"

local MpaMarkerSymbolDict = MpaTk.get_marker_symbol_dict()
symbol_scope_separator = MpaMarkerSymbolDict["symbol_scope_separator"]
symbol_inline_comment =  MpaMarkerSymbolDict["symbol_inline_comment"]
symbol_section_separator = MpaMarkerSymbolDict["symbol_section_separator"]
symbol_system_path_separtor = MpaMarkerSymbolDict["symbol_system_path_separtor"]
symbol_intersection_gap = MpaMarkerSymbolDict["symbol_intersection_gap"]

if FLAG_create_test_data then
  cmd = "python create_sample_data.py"
  os.execute(cmd)
end

-------------------------------------------------------------------
function add_global_parameters(dict_global_parameters)
    -- Add global parameters

    -- External dependencies
    dict_global_parameters["USE LATEX"] = "True"
    dict_global_parameters["USE SCIPY"] = "True"

    -- Figure
    --   Add twin axis
    -- dict_global_parameters["TWINX AXIS SOURCE INDEX LIST"] = "((0,0))"
    dict_global_parameters["FIGURE OUTPUT FILE NAME"] = file_name_output
    dict_global_parameters["FIGURE TITLE FONT SIZE"] = 40
    dict_global_parameters["FIGURE NUMBER OF ROWS"] = 3
    dict_global_parameters["FIGURE NUMBER OF COLUMNS"] = 1
    dict_global_parameters["FIGURE SHARE X"] = "False"
    dict_global_parameters["FIGURE SHARE Y"] = "False"
    dict_global_parameters["FIGURE LENGTH"] = 10
    dict_global_parameters["FIGURE HEIGHT"] = 20
    dict_global_parameters["FIGURE SUBPLOTS VERTICAL SPACING"] = 0
    dict_global_parameters["FIGURE SUBPLOTS HORIZONTAL SPACING"] = 0

    -- Labels
    dict_global_parameters["FIGURE AXIS LABEL ON"] = "True"
    dict_global_parameters["FIGURE X LABEL"]   = "Time (ns)"
    dict_global_parameters["FIGURE Y LABEL"]   = "RMSD ($\\mathrm{\\AA}$)" -- Angstrom's unicode is \u212B in python
    dict_global_parameters["FIGURE X LABEL PADDING"] = 60
    dict_global_parameters["FIGURE Y LABEL PADDING"] = 60

end



-------------------------------------------------------------------
function add_local_parameters(dict_local_parameters, dict_specs)

      
      -- Panel
      dict_local_parameters["PANEL BOX SHAPE"] = "round"
      dict_local_parameters["PANEL BOX LINE WIDTH"] = 5

      -- Ticks
      dict_local_parameters["HIDE OVERLAPPING Y TICK LABEL"] = "True"

      table.insert(list_local, string.format("PANEL LABEL: %s", panel_label))
      table.insert(list_local, string.format("PANEL LABEL COORDINATE: %s", panel_label_coordinate))

      -- Lines
      dict_global_parameters["LINE STYLE"]  = '-'
      dict_global_parameters["LINE OPACITY"] = 0.3
      dict_global_parameters["COLOR ORDER"] = "(k, r, g, b, m)"
      dict_global_parameters["lINE SHOW BLOCK AVERAGED LINE"] = "True"
      dict_global_parameters["LINE BLOCK AVERAGED LINE WIDTH"] = 2


end

--------------------------------------------------------------------------
----------------------------------- MAIN ---------------------------------
--------------------------------------------------------------------------
if ID_test_case == 1 then
      local dir_output = dir_figure_root
      local file_plot_config = "plot.config"
      local file_name_output = "output.png"
      file_plot_config = table.concat({dir_output, file_plot_config}, '/')
      file_name_output = table.concat({dir_output, file_name_output}, '/')

      --------------------------------------------------------------------
      -- Step 1. File parameters
      --------------------------------------------------------------------

      local section_title = "[[DATA]]"
      local dict_data_parameters = {}

      local list_input_file_names = {"data1.dat", "data2.dat", "data3.dat", "data4.dat"}
      local list_legends = {"data1", "data2", "data3", 'data4'}
      local list_legend_panel_indices = {"(0,0)", "(1,0)", "(2,0)", "(2,0)"}
      local list_legend_anchor_coordinates = {"(0.98, 0.95)", "(0.98, 0.95)", "(0.51, 0.95)", "---"}
      local list_legend_number_of_columns = {1,1,2,"---"}
      local list_line_panel_indices = {"(0,0)", "(1,0)", "(2,0)", "(2,0)"}
      local list_block_average_block_size = {10,2,100,50}

      local list_panel_labels = {'A', "B", "C", "D"}
      local panel_label_coordinates = "(0.05, 0.9)"
      local list_panel_label_coordinates = {panel_label_coordinates, panel_label_coordinates,
                panel_label_coordinates, panel_label_coordinates}

      local dict_min_max = {x_min="None", x_max=1.9, y_min="None", y_max=3.0}
      for i,file_name in pairs(list_input_file_names)  do
        local full_file_path =  table.concat({dir_data_root, file_name}, '/')
        local global_key = MpaTk.list_last_item(MpaTk.split(full_file_path, '/'))
        dict_data_parameters[global_key] = {}
        dict_data_parameters[global_key]["DATA FILE"] = full_file_path
        dict_data_parameters[global_key]["DATA LEGEND"] = list_legends[i]
        dict_data_parameters[global_key]["DATA LEGEND PANEL INDICES"] = list_legend_panel_indices[i]
        dict_data_parameters[global_key]["DATA PANEL INDICES"] = list_line_panel_indices[i]
        dict_data_parameters[global_key]["DATA BLOCK AVERAGE BLOCK SIZE"] = list_block_average_block_size[i]
        dict_data_parameters[global_key]["DATA SHOW BLOCK AVERAGE"] = "True"
      end

      MpaTk.write_section_header(file_plot_config, section_title, symbol_section_separator, 'w')
      local write_mode = 'a'
      MpaTk.write_dict2d_to_file(file_plot_config, dict_data_parameters, write_mode, symbol_scope_separator, symbol_inline_comment)
      print("File parameters: ", file_plot_config)


      --------------------------------------------------------------------
      -- Step 2. Global plotting parameters
      --------------------------------------------------------------------
      local section_title = "[[GLOBAL]]"
  		local dict_global_parameters = {}
      local write_mode = 'a'
      dict_global_parameters["GLOBAL PARAMETERS"] = {}

      add_global_parameters(dict_global_parameters["GLOBAL PARAMETERS"])

      MpaTk.write_intersection_gap(file_plot_config, symbol_intersection_gap, write_mode)
      MpaTk.write_section_header(file_plot_config, section_title, symbol_section_separator, write_mode)
      MpaTk.write_dict2d_to_file(file_plot_config, dict_global_parameters, write_mode, symbol_scope_separator, symbol_inline_comment)
  		print("Global parameters: ", file_plot_config)

      --------------------------------------------------------------------
      -- Step 3. Local plotting parameters
      --------------------------------------------------------------------
      local section_title = "[[LOCAL]]"
      local dict_local_parameters = {}
      local list_panel_indices = {"(0,0)", "(1,0)", "(2,0)"}
      local list_panel_labels = {'A', 'B', 'C'}
      local list_x_label_decimal_places = {1, 1, 1} 
      local list_y_label_decimal_places = {2, 1, 2}
      local write_mode = 'a'

      for i = 1, #list_panel_indices do
        local panel_indices = list_panel_indices[i]
        local global_key = panel_indices
        dict_local_parameters[global_key] = {}
        dict_local_parameters[global_key]["PANEL LABEL ON"] = "True"
        dict_local_parameters[global_key]["PANEL LABEL"] = list_panel_labels[i]
        dict_local_parameters[global_key]["PANEL INDICES"] = panel_indices
        dict_local_parameters[global_key]["X TICK LABEL NUMBER OF DECIMAL PLACES"] = list_x_label_decimal_places[i]
        dict_local_parameters[global_key]["Y TICK LABEL NUMBER OF DECIMAL PLACES"] = list_y_label_decimal_places[i]
        dict_local_parameters[global_key]["X LIMIT TIGHT ON"] = "False"
        dict_local_parameters[global_key]["Y LIMIT TIGHT ON"] = "False"
        dict_local_parameters[global_key]["X TICK LABEL HIDE OVERLAP"] = "True"
        dict_local_parameters[global_key]["X TICK LABEL HIDE FIRST"] = 2
        dict_local_parameters[global_key]["X TICK LABEL HIDE LAST"] = 2        
        dict_local_parameters[global_key]["Y TICK LABEL HIDE OVERLAP"] = "True"
        dict_local_parameters[global_key]["Y TICK LABEL HIDE FIRST"] = 1
        dict_local_parameters[global_key]["Y TICK LABEL HIDE LAST"] = 1
      end
      MpaTk.write_intersection_gap(file_plot_config, symbol_intersection_gap, write_mode)
      MpaTk.write_section_header(file_plot_config, section_title, symbol_section_separator, write_mode)
      MpaTk.write_dict2d_to_file(file_plot_config, dict_local_parameters, write_mode, symbol_scope_separator, symbol_inline_comment)
      print("Local parameters: ", file_plot_config)
  		--------------------------------------------------------------------
  		-- Step 4. plot
  		--------------------------------------------------------------------
  		local in_script = "mpa.py"
        local show_preview = "yes-preview"
  		local cmd = table.concat({"python", in_script,  file_plot_config, show_preview}, " ")
  		os.execute(cmd)
      print(string.format("Output figure: %s", file_name_output))


end  	

