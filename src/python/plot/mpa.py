"""
MPA FRONTEND
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""
import sys
import os
folder_mpa_source = "MPA"
path_mpa = os.path.join(".", folder_mpa_source)
sys.path.insert(0, path_mpa )

import mpa_core as MPA 

ccc = 1
file_config = sys.argv[ccc]
ccc += 1
if len(sys.argv) > 2:
	show_preview =  sys.argv[ccc]
else:
	show_preview = "no-preview"

if show_preview == "yes-preview":
	preview = True
else:
	preview = False

MPA.main(file_config, preview)



