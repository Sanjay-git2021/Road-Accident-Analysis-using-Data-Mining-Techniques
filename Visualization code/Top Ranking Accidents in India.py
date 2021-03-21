#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\top6 accidents.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
States = df["States"]
x = np.arange(6)
fig = plt.figure(figsize=(16,8))
Total_data_2017 = df["State/UT-wise Total Number of Persons Killed in Road Accidents during - 2017"]
Total_data_2018 = df["State/UT-wise Total Number of Persons Killed in Road Accidents during - 2018"]
#plt.bar(x=df["States"],height=df["State/UT-wise Total Number of Persons Killed in Road Accidents during - 2017"],color='rgbyc')
plt.xticks(x,["Uttar Pradesh","Maharashtra","Tamil Nadu","Karnataka","Madhya Pradesh","Rajasthan"],rotation=45)
width = 0.30
plt.bar(x-0.2,Total_data_2017 , width) 
plt.bar(x+0.2,Total_data_2018 , width)
plt.ylabel("Total Accidents in Year 2017 and 2018")
plt.title("State/UT-wise Total Number of Persons Killed in Road Accidents during - 2017 and 2018 ")
plt.legend(["2017","2018"])
