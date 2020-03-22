# Reads the csv file located in resources and returns a dictionary
# list of month, year, and profit loss

# import modules needed to read the csv file
import os
import csv


def Read_Data():
    # Crate the file name to pull in the data
    data_file = os.path.join('..', 'Resources', 'election_data.csv')

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
            voterID = row[0]
            county = row[1]
            candidate = row[2]

            # put the values into a dictionary item and return
            dict = {
                'voter id': row[0],
                'county': row[1],
                'candidate': row[2]
            }
            data.append(dict)

    return data

# Comment out after test
# data = Read_Data()
# print(len(data))
