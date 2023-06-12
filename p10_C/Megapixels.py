import pandas as pd
def getMegapixels():
    gM = pd.read_csv('test.csv',usecols=['id','px_width'])
    return gM.iloc[[2,12,33,55,69,84,109,119,209,399]];