# Generates an analysis of the election data

import read_election_data_file
import analyze_data
import print_analysis

# get the data from the csv file
data = read_election_data_file.Read_Data()

# analyze the data
analysis = analyze_data.AnalyzeData(data)

# print the data
print_analysis.Print_Analysis(analysis)