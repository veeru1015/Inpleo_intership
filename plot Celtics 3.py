#NBA Presentation

#Created by: Veeru Senthil
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as n

#Setting Up
nba = pd.read_csv('nba_stats.csv')
Celtics = nba[(nba['TEAM'] == 'Bos')]

plt.style.use('_mpl-gallery')


#Prep Data
Minutes = Celtics['Usage Rate']
points = Celtics['Turnover Rate']

print(points[3,5])


#fig = plt.figure()
#fig.patch.set_facecolor('grey')

#plt.scatter(Minutes, points, color = 'midnightblue' )

#plt.title('The Effect Usage Rate has on the Turnover Rate of Celtics Players')
#plt.xlabel('Usage Rate')
#plt.ylabel('Turnover Rate')
#plt.show()

