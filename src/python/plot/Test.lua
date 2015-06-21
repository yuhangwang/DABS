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



function write_str_to_file (str, output_file_name)
	-- Write a string into an output file
	local OUT = io.open(output_file_name, 'w')
	io.output(OUT)
	io.write(str)
	io.close(OUT)
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

      local OUT = io.open(file_list_of_inputs, 'w')
      io.output(OUT)
      
      local list_input_file_names = {"data1.dat", "data2.dat", "data3.dat", "data4.dat"}
      local list_legends = {"data1", "data2", "data3", 'data4'}
      local list_plot_panel_id = {"(0,0)", "(1,0)", "(2,0)", "(3,0)"}
      local list_panel_labels = {'A', "B", "C", "D"}
      local panel_label_coordinates = "(0.05, 0.8)"
      local list_panel_label_coordinates = {panel_label_coordinates, panel_label_coordinates,
                panel_label_coordinates, panel_label_coordinates}

      for i,file_name in pairs(list_input_file_names)  do
        local input_file = table.concat({dir_data_root, file_name}, '/')
        local legend = list_legends[i]
        local id_panel = list_plot_panel_id[i]
        local panel_label = list_panel_labels[i]
        local panel_label_coordinates = list_panel_label_coordinates[i]
        local line_content = string.format("%s; %s; %s; %s; %s\n", input_file, legend, id_panel, 
                      panel_label, panel_label_coordinates)
        io.write(line_content)
      end
      
      io.close(OUT)

      

      --------------------------------------------------------------------
      -- Step 2. create a file containing plotting parameters
      --------------------------------------------------------------------
  		file_plot_parameters = table.concat({dir_output, file_plot_parameters}, '/')
  		local OUT = io.open(file_plot_parameters, 'w')
  		io.output(OUT)

  		local table_parameters = {}

  		-- External dependencies
  		table_parameters["USE LATEX"] = "YES"
  		table_parameters["USE SCIPY"] = "YES"

  		-- Figure
  		-- table_parameters["FIGURE TITLE"] = "DOJF2 RMSD"
      table_parameters["FIGURE OUTPUT FILE NAME"] = file_name_output
  		table_parameters["FIGURE TITLE FONT SIZE"] = 40
  		table_parameters["FIGURE NUMBER OF ROWS"] = 4
  		table_parameters["FIGURE NUMBER OF COLUMNS"] = 1
  		table_parameters["FIGURE SHARE X"] = "YES"
  		table_parameters["FIGURE SHARE Y"] = "YES"
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
  		table_parameters["HIDE OVERLAPPING Y TICK LABEL"] = "YES"

  		-- Lines
  		table_parameters["LINE STYLE"] 	= '-'
  		table_parameters["LINE TRANSPARENCY"] = 0.3
  		table_parameters["COLOR ORDER"] = "(k, r, g, b, m)"
  		table_parameters["SHOW BLOCK AVERAGED LINE"] = "YES"
  		table_parameters["LINE BLOCK AVERAGE BLOCK SIZE"] = 50
  		table_parameters["BLOCK AVERAGED LINE WIDTH"] = 2

  		-- Legend
  		table_parameters["LEGEND FONT SIZE"] = 18
  		table_parameters["LEGEND BOX ANCHOR COORDINATE TUPLE"] = "(0.75, 0.1)"
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
  		local in_script = "PlotLines.py"
  		local cmd = table.concat({"python", in_script,  file_list_of_inputs, file_plot_parameters}, " ")
  		os.execute(cmd)


end  	

