import os

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

# send to the output file and the screen
def SendOutput(output, message):
    print(message)
    message += '\n'
    output.write(message)
    
# Define method to print out analysis
def Print_Analysis(analysis):
    with open(GetOutputFileName(), mode='w', encoding='utf-8') as output:
        SendOutput(output, "Financial Analysis")
        SendOutput(output, "----------------------------")
        SendOutput(output, f"Total Months: {analysis['total_months']}")
        SendOutput(output, f"Total: {Format_Currency(analysis['total_profile_loss'])}")
        SendOutput(output, f"Average Change: {Format_Currency(analysis['average_profit_loss_change'])}")
        SendOutput(output, f"Greatest Increase in Profits: {analysis['greatest_increase']['month']} - " + \
                f"{analysis['greatest_increase']['year']}" + \
                f"  ({Format_Currency(analysis['greatest_increase']['change_from_previous_month'])})")
        SendOutput(output, f"Greatest Decrease in Profits: {analysis['greatest_decrease']['month']} - " + \
                f"{analysis['greatest_decrease']['year']}" + \
                f"  ({Format_Currency(analysis['greatest_decrease']['change_from_previous_month'])})")
