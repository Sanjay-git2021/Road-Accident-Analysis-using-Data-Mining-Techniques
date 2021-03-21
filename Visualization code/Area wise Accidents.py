#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Area_WiseAccidents.csv')
time_data = df["Area Wise"]
Count_data = df["Residential Area count"]
explode = (0.1,0.1,0.2,0.1,0.1)
plt.pie(Count_data,labels=time_data,autopct='%1.1f%%',explode=explode,shadow=True,startangle=140)
plt.title("Area Wise - Residential Area ")
plt.show()
plt.savefig('plot.png',dpi=300,bbox_inches='tight')


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Area_WiseAccidents.csv')
time_data = df["Area Wise"]
Count_data = df["Institutional Area Count"]
explode = (0.1,0.1,0.2,0.1,0.1)
plt.pie(Count_data,labels=time_data,autopct='%1.1f%%',explode=explode,shadow=True,startangle=140)
plt.title("Area Wise - Institutional Area ")
plt.show()
plt.savefig('plot.png',dpi=300,bbox_inches='tight')


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Area_WiseAccidents.csv')
time_data = df["Area Wise"]
Count_data = df["Open Area"]
explode = (0.1,0.1,0.2,0.1,0.1)
plt.pie(Count_data,labels=time_data,autopct='%1.1f%%',explode=explode,shadow=True,startangle=140)
plt.title("Area Wise - Open Area ")
plt.show()
plt.savefig('plot.png',dpi=300,bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(7,7))
df = pd.read_csv(r'C:\Users\Karan\Desktop\final visualisation code and data\Area_WiseAccidents.csv')
time_data = df["Area Wise"]
Count_data = df["Market/Commercial Area"]
explode = (0.1,0.1,0.2,0.1,0.1)
plt.pie(Count_data,labels=time_data,autopct='%1.1f%%',explode=explode,shadow=True,startangle=140)
plt.title("Area Wise - Market/Commercial Area ")
plt.show()
plt.savefig('plot.png',dpi=300,bbox_inches='tight')
