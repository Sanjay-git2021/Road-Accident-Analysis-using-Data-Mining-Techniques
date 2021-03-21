#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

FaultType = pd.read_csv(r'C:\Users\Karan\Desktop\code\Traffic-Accident-Analysis-master\datafile_4.csv')
FaultType = FaultType.drop(FaultType.index[[34,37]])


faulttype = {}
faulttype["Driver's Fault"] = FaultType.loc[36,'Fault of Driver-Total No. of Road Accidents - 2014'] 
faulttype["Cyclist's Fault"] = FaultType.loc[36,'Fault of Cyclist-Total No. of Road Accidents - 2014'] 
faulttype["Vehicle Condition"] = FaultType.loc[36,'Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014'] 
faulttype["Road Condition"] = FaultType.loc[36,'Defect in Road Condition-Total No. of Road Accidents - 2014'] 
faulttype["Weather Condition"] = FaultType.loc[36,'Weather Condition-Total No. of Road Accidents - 2014'] 
faulttype["Passenger's Fault"] = FaultType.loc[36,'Fault of Passenger-Total No. of Road Accidents - 2014'] 
faulttype["Poor Light"] = FaultType.loc[36,'Poor light-Total No. of Road Accidents - 2014'] 
faulttype["Stray Animals"] = FaultType.loc[36,'Stray animals-Total No. of Road Accidents - 2014'] 
faulttype["Others"] = FaultType.loc[36,'Other causes/ Causes not known-Total No. of Road Accidents - 2014'] 


val = list(faulttype.values())
total = sum(val)
for i in range(0,9):
    val[i] = format(val[i]*100/total,'.2f')

plt.figure(figsize=(10,8))
plt.pie(list(faulttype.values()))
plt.axis('equal')
plt.xlabel('Accidents in 2014')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
label = [list(pair) for pair in zip(list(faulttype.keys()),val)]
plt.legend(label,loc="best")
plt.show()

