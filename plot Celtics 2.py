#NBA Presentation

#Created by: Veeru Senthil
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

#Setting Up
nba = pd.read_csv('nba_stats.csv')
Celtics = nba[(nba['TEAM'] == 'Bos')]

plt.style.use('_mpl-gallery')

#Line Graph

#Prep Data
Minutes = nba['MPG']
points = nba['PPG']


fig = plt.figure()
fig.patch.set_facecolor('lavender')

plt.scatter(Minutes, points, color = 'navy' )
plt.title('Points per game of all NBA Players with Varying Minutes')
plt.xlabel('Minutes per Game')
plt.ylabel('Points per Game')
plt.show()

print('Hii ')