#NBA Presentation Preparation

#Created by: Veeru Senthil
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

#Setting Up
nba = pd.read_csv('nba_stats.csv')
Celtics = nba[(nba['TEAM'] == 'Bos')]

plt.style.use('_mpl-gallery')



#Setting up data

Position = Celtics['POS']

count = Position.value_counts()

count_df = pd.DataFrame(count)
#print(count_df)

count_df['position'] = count_df.index
count_df.columns = ['count' , 'position']

#print(count_df)

#Setting up Chart

fig, ax = plt.subplots(figsize=(30, 6))

ax.bar(count_df['position'], count_df['count'])

ax.set(title = "Positions of Boston Celtics Players",
        xlabel = 'Position',
        ylabel = 'Frequency')


plt.show()


