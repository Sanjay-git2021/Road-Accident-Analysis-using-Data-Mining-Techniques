#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,4))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Weather data.csv')
weather_type = df["Weather Condition"]
Total_data = df["No of Accidents - 2017"]
PersonKilled_data = df["Persons Killed - 2017"]
PersonInjured_data = df["Persons Injured - 2017"]

plt.bar(x=df["Weather Condition"],height=df["No of Accidents - 2017"],color='rgbyc')
plt.xticks(rotation=45)
plt.ylabel("Number  ")
plt.title("Number of Road Accidents in India according to Weather conditions ")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
fig = plt.figure(figsize=(16,8))
x = np.arange(5)
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Weather data.csv')
Weather_data = df["Weather Condition"]
Count_data = df["No of Accidents - 2017"]
injured_data = df["Persons Injured - 2017"]
person_killed = df["Persons Killed - 2017"]
width = 0.30
plt.xticks(x,["Sunny or Clear","Rainy", "Foggy and  Misty","Hail or Sleet","Others"],rotation=45)
plt.bar(x-0.2, Count_data, width) 
plt.bar(x+0.2, injured_data, width)
plt.bar(x+0.4, person_killed, width)
plt.xlabel("Weather Conditions") 
plt.ylabel("Counts in numbers") 
plt.legend(["No of Accidents", "Number of People injured", "Number of person killed"]) 
