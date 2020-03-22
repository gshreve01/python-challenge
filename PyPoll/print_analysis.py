# prints out the analysis to screen and to a file

import os
import sys

sys.path.insert(1, '../Common')
import common

# taken as example to force generation of output directory from stack overflow
# https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
def GetOutputFileName():
    filename = os.path.join("..", "output", "ElectionResults.txt")
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return filename

# Format Percentage
def Format_Percentage(value):
    value = float(value)
    return '{:,.3f}'.format(round(value*100, 3))

# Define method to print out analysis
def Print_Analysis(analysis):
    with open(GetOutputFileName(), mode='w', encoding='utf-8') as output:
        common.SendOutput(output, "Election Results")
        common.SendOutput(output, "----------------------------")
        common.SendOutput(output, f"Total Votes: {analysis['total_votes']}")
        common.SendOutput(output, "----------------------------")
        for candidate in analysis['candidates']:
            common.SendOutput(output, f"{candidate['candidate']}:  " + \
                f"{Format_Percentage(candidate['vote_percentage'])}% " + \
                f"({candidate['number_of_votes']})")
        common.SendOutput(output, "----------------------------")
        common.SendOutput(output, f"Winner: {analysis['winningCandidate']['candidate']}")
        common.SendOutput(output, "----------------------------")
