#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Timebase2014.csv')
time_data = df["Time"]
Count_data = df["2014"]
explode = (0,0,0,.2,0,0,0,0)
plt.pie(Count_data,labels=time_data,autopct='%1.2f%%',explode=explode,shadow=True,startangle=140)
plt.title("Time Zone wise year-2014")
plt.show()
plt.savefig('plot.png',dpi=300,bbox_inches='tight')
