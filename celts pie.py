#PIE NBA

from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Setting Up
nba = pd.read_csv('nba_stats.csv')
Celtics = nba[(nba['TEAM'] == 'Bos')]

rel = Celtics['Availability']


counts = rel.value_counts()

count_df = pd.DataFrame(counts)
#print(count_df)

count_df['Availability Index'] = count_df.index
count_df.columns = ['count' , 'Availability Index']


#Setting up Chart

av = count_df['Availability Index']

fig, ax = plt.subplots()

ax.set(title = "Availability Rankings of NBA Players")


ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))


plt.pie(count_df['count'], labels = count_df['Availability Index'], autopct='%.1f%%')

plt.show()


