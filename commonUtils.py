ON = 'on'
OFF = 'off'

def getContentWithBraces(value):
    return str(value).split("(")[1].split(")")[0]

def getContentWithQuotes(value):
    return str(value).split("\"")[1]