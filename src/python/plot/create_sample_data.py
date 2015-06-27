"""
Create sample data
Author: Yuhang Wang
Date: 06/20/2015
"""
import numpy
import os

dir_output = "data"
dir_current = os.path.realpath(".")

list_file_names = ["data1.dat", "data2.dat", "data3.dat", "data4.dat"]
list_data = []
number_of_sample_points = 500
data_start = 0
data_end = numpy.pi/2

mean = 0
std = 0.2
noise = numpy.random.normal(loc=mean, scale=std,size=number_of_sample_points)
X = numpy.linspace(data_start,data_end,number_of_sample_points) 
list_data.append([[X[i], numpy.sin(X[i])+noise[i]] for i in range(number_of_sample_points)])
list_data.append([[X[i], numpy.cos(X[i])+noise[i]] for i in range(number_of_sample_points)])
list_data.append([[X[i], numpy.tanh(X[i])+noise[i]] for i in range(number_of_sample_points)])
list_data.append([[200*X[i], numpy.cosh(X[i])+noise[i]] for i in range(number_of_sample_points)])

for i in range(len(list_data)):
	file_name = os.path.join(dir_current, dir_output, list_file_names[i])
	data = list_data[i]
	numpy.savetxt(file_name,data)
