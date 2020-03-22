# Generates an analysis based on the budget data

import read_budget_data_file
import analyze_data
import print_analysis

# get the data from the csv file
data = read_budget_data_file.Read_Budget()
analysis = analyze_data.AnalyzeData(data)
print_analysis.Print_Analysis((analysis))




