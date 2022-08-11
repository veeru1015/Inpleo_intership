# Pie Chart
#Veeru Senthil


from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Setting Up
plt.style.use('_mpl-gallery')
fifa = pd.read_csv('ManUnited.csv')

#Setting up data

bodyType = fifa['body_type']

counts = bodyType.value_counts()

count_df = pd.DataFrame(counts)
#print(count_df)

count_df['Frame'] = count_df.index
count_df.columns = ['count' , 'Frame']


#Setting up Chart

labelsManU = count_df['Frame']

fig, ax = plt.subplots()

ax.set(title = "Body Types of Man United Players")


ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))


plt.pie(count_df['count'], labels = count_df['Frame'], autopct='%.1f%%')

plt.show()
