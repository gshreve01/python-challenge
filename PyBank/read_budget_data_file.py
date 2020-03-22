# Reads the csv file located in resources and returns a dictionary
# list of month, year, and profit loss

# import modules needed to read the csv file
import os
import csv

def Read_Budget():
    # Crate the file name to pull in the data
    data_file = os.path.join('..', 'Resources', 'budget_data.csv')

    # define a list that will be used to return the data
    data = []

    # Open the file
    with open(data_file) as csvFile:
        # create a csv reader
        csvReader = csv.reader(csvFile)

        # the first row is the header row, so skip
        csv_header = next(csvReader)

        # iterate through csvReader to populate the data
        for row in csvReader:
            monthYear = row[0]
            profitLoss = row[1]

            # split the month year into seperate values
            values = monthYear.split('-')

            # put the values into a dictionary item and return
            dict = {
                    'month': values[0],
                     'year': values[1],
                     'profit_loss': float(profitLoss)
                     }
            data.append(dict)

    return data


# Comment out after test
#data = Read_Budget()
#print(data)