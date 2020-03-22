# function that will return a list of values from a dictionary list.
def SplitDictionaryKeyToList(data, key):
    dataitems = []
    for item in data:
        dataitems.append(item[key])
    return dataitems

# send to the output file and the screen
def SendOutput(output, message):
    print(message)
    message += '\n'
    output.write(message)