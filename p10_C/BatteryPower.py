import pandas as pd
def getBatteryPower():
    gBP = pd.read_csv('test.csv',usecols=['id','battery_power'])
    return gBP.iloc[[2,12,33,55,69,84,109,119,209,399]];

