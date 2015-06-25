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

dir_data_root = "./data"
dir_figure_root = "./figure"



function write_str_to_file (output_file_name, str)
	-- Write a string into an output file
	local OUT = io.open(output_file_name, 'w')
	io.output(OUT)
	io.write(str)
	io.close(OUT)
end

function  update_input_information_list(list_target, file_input, legend,legend_anchor_coordinate, legend_panel_indices, legend_number_of_columns, panel_indices, panel_label, panel_label_coordinate, dict_min_max)
  -- Update the input information list
  local x_min = "None"
  local x_max = "None"    
  local y_min = "None"
  local y_max = "None"
  if dict_min_max ~= nil then
    x_min = dict_min_max["x_min"]
    x_max = dict_min_max["x_max"]
    y_min = dict_min_max["y_min"]
    y_max = dict_min_max["y_max"]
  end
  local list_local = {}
  table.insert(list_local, string.format("FILE: %s", file_input))
  table.insert(list_local, string.format("LEGEND: %s", legend))
  table.insert(list_local, string.format("LEGEND ANCHOR COORDINATE: %s", legend_anchor_coordinate))
  table.insert(list_local, string.format("LEGEND PANEL INDICES: %s", legend_panel_indices))
  table.insert(list_local, string.format("LEGEND NUMBER OF COLUMNS: %s", legend_number_of_columns))
  table.insert(list_local, string.format("PANEL INDICES: %s", panel_indices))
  table.insert(list_local, string.format("PANEL LABEL: %s", panel_label))
  table.insert(list_local, string.format("PANEL LABEL COORDINATE: %s", panel_label_coordinate))
  table.insert(list_local, string.format("X MIN: %s", x_min))
  table.insert(list_local, string.format("X MAX: %s", x_max))
  table.insert(list_local, string.format("Y MIN: %s", y_min))
  table.insert(list_local, string.format("Y MAX: %s", y_max))
  table.insert(list_target, table.concat(list_local, '; '))
end

if FLAG_create_test_data then
  cmd = "python create_sample_data.py"
  os.execute(cmd)
end

if ID_test_case == 1 then
      local dir_output = dir_figure_root
      local file_list_of_inputs = "input_file_names.list"
  		local file_plot_parameters = "plot.param"
      local file_name_output = "output.png"
      file_name_output = table.concat({dir_output, file_name_output}, '/')

      -------------------------------------------------------------------
      -- Step 1. create a file containing a list of input file names -----
      --------------------------------------------------------------------
      file_list_of_inputs = table.concat({dir_output, file_list_of_inputs}, '/')

      local list_input_file_parameters = {}
      local list_input_file_names = {"data1.dat", "data2.dat", "data3.dat", "data4.dat"}
      local list_legends = {"data1", "data2", "data3", 'data4'}
      local list_legend_panel_indices = {"(0,0)", "(1,0)", "(2,0)", "(2,0)"}
      local list_legend_anchor_coordinates = {"(0.98, 0.95)", "(0.98, 0.95)", "(0.51, 0.95)", "---"}
      local list_legend_number_of_columns = {1,1,2,"---"}
      local list_panel_indices = {"(0,0)", "(1,0)", "(2,0)", "(2,0)"}
      local list_panel_labels = {'A', "B", "C", "D"}

      local panel_label_coordinates = "(0.05, 0.9)"
      local list_panel_label_coordinates = {panel_label_coordinates, panel_label_coordinates,
                panel_label_coordinates, panel_label_coordinates}

      local dict_min_max = {x_min="None", x_max=1.9, y_min="None", y_max=3.0}
      for i,file_name in pairs(list_input_file_names)  do
        local file_input = table.concat({dir_data_root, file_name}, '/')
        local legend = list_legends[i]
        local legend_anchor_coordinate = list_legend_anchor_coordinates[i]
        local legend_panel_indices = list_legend_panel_indices[i]
        local legend_number_of_columns = list_legend_number_of_columns[i]
        local panel_indices = list_panel_indices[i]
        local panel_label = list_panel_labels[i]
        local panel_label_coordinate = list_panel_label_coordinates[i]
        update_input_information_list(list_input_file_parameters, file_input, legend, legend_anchor_coordinate, legend_panel_indices, legend_number_of_columns, panel_indices, panel_label, panel_label_coordinate, dict_min_max)
      end
      
      local text_body = table.concat(list_input_file_parameters, '\n')
      write_str_to_file(file_list_of_inputs, text_body)
      print("Input file parameters: ", file_list_of_inputs)

      --------------------------------------------------------------------
      -- Step 2. create a file containing plotting parameters
      --------------------------------------------------------------------
  		file_plot_parameters = table.concat({dir_output, file_plot_parameters}, '/')
  		local OUT = io.open(file_plot_parameters, 'w')
  		io.output(OUT)

  		local table_parameters = {}

  		-- External dependencies
  		table_parameters["USE LATEX"] = "True"
  		table_parameters["USE SCIPY"] = "True"

  		-- Figure
  		-- table_parameters["FIGURE TITLE"] = "DOJF2 RMSD"
      table_parameters["FIGURE OUTPUT FILE NAME"] = file_name_output
  		table_parameters["FIGURE TITLE FONT SIZE"] = 40
  		table_parameters["FIGURE NUMBER OF ROWS"] = 3
  		table_parameters["FIGURE NUMBER OF COLUMNS"] = 1
  		table_parameters["FIGURE SHARE X"] = "True"
  		table_parameters["FIGURE SHARE Y"] = "True"
  		table_parameters["FIGURE LENGTH"] = 10
  		table_parameters["FIGURE HEIGHT"] = 20

      -- Panel
      table_parameters["PANEL BOX SHAPE"] = "round"
      table_parameters["PANEL BOX LINE WIDTH"] = 5

  		-- Labels
  		table_parameters["X LABEL"] 	= "Time (ns)"
  		table_parameters["Y LABEL"] 	= "RMSD ($\\mathrm{\\AA}$)" -- Angstrom's unicode is \u212B in python
  		table_parameters["X LABEL PADDING"] = 40
  		table_parameters["Y LABEL PADDING"] = 60

  		-- Ticks
  		table_parameters["X TICK LABEL NUMBER OF DECIMAL PLACES"] = 1
  		table_parameters["HIDE OVERLAPPING Y TICK LABEL"] = "True"

  		-- Lines
  		table_parameters["LINE STYLE"] 	= '-'
  		table_parameters["LINE TRANSPARENCY"] = 0.3
  		table_parameters["COLOR ORDER"] = "(k, r, g, b, m)"
  		table_parameters["SHOW BLOCK AVERAGED LINE"] = "True"
  		table_parameters["LINE BLOCK AVERAGE BLOCK SIZE"] = 50
  		table_parameters["BLOCK AVERAGED LINE WIDTH"] = 2

  		-- Legend
      table_parameters["LEGEND ON"] = "True"
  		table_parameters["LEGEND FONT SIZE"] = 18
  		table_parameters["LEGEND FONT WEIGHT"] = 0

  		for key, value in pairs(table_parameters) do
  			local msg = string.format("%s: %s\n", key, value)
  			io.write(msg)
  		end

  		io.close(OUT)
  		print("Input file 2: ", file_plot_parameters)

  		--------------------------------------------------------------------
  		-- Step 3. plot
  		--------------------------------------------------------------------
  		local in_script = "mpa.py"
      local show_preview = "yes-preview"
  		local cmd = table.concat({"python", in_script,  file_list_of_inputs, file_plot_parameters, show_preview}, " ")
  		os.execute(cmd)
      print(string.format("Output figure: %s", file_name_output))


end  	

