#Veeru Senthil

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Setting Up
plt.style.use('_mpl-gallery')
fifa = pd.read_csv('ManUnited.csv')

#Setting up data

nat = fifa['nationality_name']
count = nat.value_counts()

count_df = pd.DataFrame(count)
#print(count_df)

count_df['nationality'] = count_df.index
count_df.columns = ['count' , 'nationality']

#print(count_df)

#Setting up Chart

fig, ax = plt.subplots(figsize=(30, 6))

ax.bar(count_df['nationality'], count_df['count'])

ax.set(title = "Nationalities of Manchester United Players",
        xlabel = 'Nationality',
        ylabel = 'Frequency')





plt.show()



