import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import BatteryPower as bp
import ClockSpeed as cs
import Megapixels as mp

print("----------------------")
print(cs.getClockSpeed())
print("----------------------")
print(bp.getBatteryPower())
print("----------------------")
print(mp.getMegapixels())
def main():

    def MP():
        gM = mp.getMegapixels()

        X = list(gM.iloc[:, 0])
        Y = list(gM.iloc[:, 1])

        bars = plt.bar(X, Y, color="red")
        plt.title("MegaPixeles")
        plt.xlabel("Id Megapixeles")
        plt.ylabel("Megapixeles")
        plt.legend([bars],["MegaPixeles"])
        plt.show()

    def BP():
        gBP = bp.getBatteryPower()

        X = list(gBP.iloc[:, 0])
        Y = list(gBP.iloc[:, 1])

        bars = plt.bar(X, Y, color="yellow")
        plt.title("Battery_Powder")
        plt.xlabel("Id Battery Powder")
        plt.ylabel("Battery Powder")
        plt.legend([bars], ["Battery_Powder"])
        plt.show()

    def CS():
        gCS = cs.getClockSpeed()

        X = list(gCS.iloc[:, 0])
        Y = list(gCS.iloc[:, 1])

        bars = plt.bar(X, Y, color="purple")
        plt.title("Clock_Speed")
        plt.xlabel("Id Clock_Speed")
        plt.ylabel("Clock_Speed")
        plt.legend([bars],["Clock_Speed"])
        plt.show()

    MP()
    BP()
    CS()

main()

