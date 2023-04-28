'''
Author: <Diego Colon>
Date: <4/24/23>
Class: ISTA 131
Section Leader: <Jacquie Kuru>
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a pandas dataframe
df = pd.read_csv('Final_CSV.csv', encoding='ISO-8859-1')

# group the data by genre and calculate the total number of tournaments for each genre
grouped_df = df.groupby('Genre')['TournamentNo'].sum()

# sort the data by number of tournaments in descending order
grouped_df = grouped_df.sort_values(ascending=False)

#strcuters the graph within frame of vision
fig, ax = plt.subplots(figsize=(10, 8))
fig.subplots_adjust(top=0.94,
bottom = 0.095,
left = 0.320,
right = 0.950,
hspace = 0.2,
wspace = 0.2)

# create random color for the bars
colors = np.random.rand(len(grouped_df), 3)

# create a bar plot of the number of tournaments for each genre with color map
plt.barh(grouped_df.index, grouped_df.values, color=colors)

# add horizontal lines to show exactly where the bar ends
for i, v in enumerate(grouped_df.values):
    ax.text(v + 3, i - 0.15, str(v), color='gray', fontweight='bold')
    ax.axhline(i, color='gray', linewidth=0)

# set the plot title and labels
plt.title('Number of Tournaments by Genre in ESports')
plt.xlabel('Number of Tournaments')
plt.ylabel('Genre')

# display the plot
plt.show()
