import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

data = pd.read_csv(r'C:\Users\WizardX\Desktop\data\500dailyKD.csv',skipfooter=3)
closeprice = data.CLOSE
openprice = data.OPEN
highprice = data.HIGH
lowprice = data.LOW

cci84 = talib.CCI(highprice,lowprice,closeprice,timeperiod=84)
pct = data.PCT_CHG
# diff = talib.EMA(closeprice,40) - talib.EMA(closeprice,84)
# dea = talib.EMA(diff,18)
HHV = []
LLV = []

for i in range(len(closeprice)):
    if i <= 39:
        HHV.append(0)
        LLV.append(0)
    else:
        HHV.append(max(closeprice[i-39:i]))
        LLV.append(min(closeprice[i-39:i]))

# ma60 = talib.MA(closeprice,60)
df = pd.DataFrame(zip(cci84[83:],pct[83:],closeprice[83:],ma60[83:]),
                  columns=('cci','pct','closep','ma'),index = [data.DateTime[83:]])

# sig = []


# df['SIG'] = sig
# a = df.SIG.shift(1)*df['pct']
# print(a.sum())
# a.cumsum().plot()
# df.pct.cumsum().plot()
