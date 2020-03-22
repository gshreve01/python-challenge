# Take budge data and return analysis in dictionary item
def AnalyzeData(data):
    total_months = len(data)

    # create a place holder for greatest increases and decreases
    previous_P_and_L = data[0]
    greatest_decrease = previous_P_and_L
    greatest_increase = previous_P_and_L
    total_profit_loss = 0
    for p_and_l in data:
        # total the profit loss
        total_profit_loss += p_and_l['profit_loss']

        # calculate the change and store it in the dictionary item
        p_and_l['change_from_previous_month'] = p_and_l['profit_loss'] - previous_P_and_L['profit_loss']

        # determine if this is the greatest increase
        if p_and_l['change_from_previous_month'] > greatest_increase['change_from_previous_month']:
            greatest_increase = p_and_l
        # else it could be the greatest decrease
        elif p_and_l['change_from_previous_month'] < greatest_decrease['change_from_previous_month']:
            greatest_decrease = p_and_l
        # set the comparison for next loop
        previous_P_and_L = p_and_l

    all_changes = SplitDictionaryKeyToList(data, 'change_from_previous_month')
    total_changes = sum(all_changes)
    # remember that the first month did not have changes
    average_change = total_changes / (total_months - 1)
    return {
        'total_months' : total_months,
        'total_profile_loss' : total_profit_loss,
        'average_profit_loss_change' : average_change,
        'greatest_decrease' : greatest_decrease,
        'greatest_increase': greatest_increase
    }

# function that will return a list of values from a dictionary list.
def SplitDictionaryKeyToList(data, key):
    dataitems = []
    for item in data:
        dataitems.append(item[key])
    return dataitems