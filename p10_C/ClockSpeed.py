import pandas as pd
def getClockSpeed():
    gCS = pd.read_csv('test.csv',usecols=['id','clock_speed'])
    return gCS.iloc[[2,12,33,55,69,84,109,119,209,399]];