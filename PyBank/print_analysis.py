# prints out the analysis to screen and to a file

import os
import sys

# from a lot of pain to eventually read on a hack method.....
sys.path.insert(1, '../Common')
import common

# taken from stack overflow - https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
def Format_Currency(amount):
    amount = float(amount)
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# taken as example to force generation of output directory from stack overflow
# https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
def GetOutputFileName():
    filename = os.path.join("..", "output", "AnalysisResults.txt")
    if not os.path.exists(os.path.dirname(filename)):
        try:
           os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return filename

# Define method to print out analysis
def Print_Analysis(analysis):
    with open(GetOutputFileName(), mode='w', encoding='utf-8') as output:
        common.SendOutput(output, "Financial Analysis")
        common.SendOutput(output, "----------------------------")
        common.SendOutput(output, f"Total Months: {analysis['total_months']}")
        common.SendOutput(output, f"Total: {Format_Currency(analysis['total_profile_loss'])}")
        common.SendOutput(output, f"Average Change: {Format_Currency(analysis['average_profit_loss_change'])}")
        common.SendOutput(output, f"Greatest Increase in Profits: {analysis['greatest_increase']['month']} - " + \
                f"{analysis['greatest_increase']['year']}" + \
                f"  ({Format_Currency(analysis['greatest_increase']['change_from_previous_month'])})")
        common.SendOutput(output, f"Greatest Decrease in Profits: {analysis['greatest_decrease']['month']} - " + \
                f"{analysis['greatest_decrease']['year']}" + \
                f"  ({Format_Currency(analysis['greatest_decrease']['change_from_previous_month'])})")
