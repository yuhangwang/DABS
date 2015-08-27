"""
Get the histogram for an input data series
AUTHOR: YUHANG WANG
DATE: 07-08-2015
UPDATE: multiply the normalized bin heights by bin size 
	make the sum of bin heights equal to one
	instead of letting the integration of the 
	whole range equal to one.
"""


import sys
import numpy

ccc = 1
file_input = sys.argv[ccc]
ccc = ccc + 1
file_output = sys.argv[ccc]
ccc = ccc + 1
which_data_column = int(sys.argv[ccc])
ccc = ccc + 1
histogram_lower_bound = float(sys.argv[ccc])
ccc = ccc + 1
histogram_upper_bound = float(sys.argv[ccc])
ccc = ccc + 1
histogram_bin_size = float(sys.argv[ccc])


raw_data = numpy.loadtxt(file_input)
data = raw_data[:,which_data_column-1]

number_of_bins = int(numpy.ceil((histogram_upper_bound - histogram_lower_bound)/float(histogram_bin_size)))
histogram_range = (histogram_lower_bound, histogram_upper_bound)

flag_make_normalized_histogram = True
histogram_data, histogram_edges = numpy.histogram(data, bins=number_of_bins, range=histogram_range, density=flag_make_normalized_histogram)

number_of_data_rows = numpy.shape(histogram_data)[0]
number_of_data_columns = 2
data_output = numpy.zeros((number_of_data_rows, number_of_data_columns))

array_bin_sizes = histogram_edges[1:] - histogram_edges[0:-1]
data_output[:,0] = histogram_edges[1:] # note: histogram_edges has an extra item to mark the starting point of the range
data_output[:,1] = histogram_data * array_bin_sizes

numpy.savetxt(file_output, data_output)

