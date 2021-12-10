import statistics 
import pandas as pa
import csv

df = pa.read_csv('StudentsPerformance.csv')

math = df["math score"].to_list()
write = df["reading score"].to_list()
read = df["writing score"].to_list()

math_mean = statistics.mean(math)
write_mean = statistics.mean(write)
read_mean = statistics.mean(read)

math_median = statistics.mean(math)
write_median = statistics.mean(write)
read_median = statistics.mean(read)

math_mode = statistics.mean(math)
read_mode = statistics.mean(read)
write_mode = statistics.mean(write)

print("Mean, Median, Mode of Maths score is {}, {}, {} resp.".format(math_mean, math_median, math_mode))
print("Mean, Median, Mode of Writing score is {}, {}, {} resp.".format(read_mean, read_median, read_mode))
print("Mean, Median, Mode of Reading score is {}, {}, {} resp.".format(write_mean, write_median, write_mode))

math_stDev = statistics.stdev(math)
write_stDev = statistics.stdev(write)
read_stDev = statistics.stdev(read)

math_1_stdev_start, math_1_stdev_end = math_mean - math_stDev, math_mean + math_stDev 
math_2_stdev_start, math_2_stdev_end = math_mean-(2*math_stDev), math_mean +(2*math_stDev)
math_3_stdev_start, math_3_stdev_end = math_mean-(3*math_stDev), math_mean +(3*math_stDev)

write_1_stdev_start, write_1_stdev_end = write_mean - write_stDev, write_mean + write_stDev 
write_2_stdev_start, write_2_stdev_end = write_mean-(2*write_stDev), write_mean +(2*write_stDev)
write_3_stdev_start, write_3_stdev_end = write_mean-(3*write_stDev), write_mean +(3*write_stDev)

read_1_stdev_start, read_1_stdev_end = read_mean - read_stDev, read_mean + read_stDev 
read_2_stdev_start, read_2_stdev_end = read_mean-(2*read_stDev), read_mean +(2*read_stDev)
read_3_stdev_start, read_3_stdev_end = read_mean-(3*read_stDev), read_mean +(3*read_stDev)

math_data_in1st_stdev = [result for result in math if result > math_1_stdev_start and result <math_1_stdev_end]
math_data_in2nd_stdev = [result for result in math if result > math_2_stdev_start and result <math_2_stdev_end]
math_data_in3rd_stdev = [result for result in math if result > math_3_stdev_start and result <math_3_stdev_end]

read_data_in1st_stdev = [result for result in read if result > read_1_stdev_start and result <read_1_stdev_end]
read_data_in2nd_stdev = [result for result in read if result > read_2_stdev_start and result <read_2_stdev_end]
read_data_in3rd_stdev = [result for result in read if result > read_3_stdev_start and result <read_3_stdev_end]

write_data_in1st_stdev = [result for result in write if result > write_1_stdev_start and result <write_1_stdev_end]
write_data_in2nd_stdev = [result for result in write if result > write_2_stdev_start and result <write_2_stdev_end]
write_data_in3rd_stdev = [result for result in write if result > write_3_stdev_start and result <write_3_stdev_end]

print("{}% of data for math scores lies in 1st standard deviation".format(len(math_data_in1st_stdev)*100/len(math)))
print("{}% of data for math scores lies in 2nd standard deviation".format(len(math_data_in2nd_stdev)*100/len(math)))
print("{}% of data for math scores lies in 3rd standard deviation".format(len(math_data_in3rd_stdev)*100/len(math)))

print("{}% of data for writing scores lies in 1st standard deviation".format(len(write_data_in1st_stdev)*100/len(write)))
print("{}% of data for writing scores lies in 2nd standard deviation".format(len(write_data_in2nd_stdev)*100/len(write)))
print("{}% of data for writing scores lies in 3rd standard deviation".format(len(write_data_in3rd_stdev)*100/len(write)))

print("{}% of data for reading scores lies in 1st standard deviation".format(len(read_data_in1st_stdev)*100/len(read)))
print("{}% of data for reading scores lies in 2nd standard deviation".format(len(read_data_in2nd_stdev)*100/len(read)))
print("{}% of data for reading scores lies in 3rd standard deviation".format(len(read_data_in3rd_stdev)*100/len(read)))