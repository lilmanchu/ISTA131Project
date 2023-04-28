'''
Author: <Diego Colon>
Date: <4/24/23>
Class: ISTA 131
Section Leader: <Jacquie Kuru>
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors

# Read CSV file into a pandas dataframe
df = pd.read_csv('Final_CSV.csv', encoding = 'ISO-8859-1')

# sorts the rows of a pandas DataFrame df in descending order according to the values in the 'TotalMoney' column and then selects the top 10 rows with the highest 'TotalMoney' values
df_top10 = df.sort_values('TotalMoney', ascending=False).head(10)

# strcuters the graph within frame of vision
fig, ax = plt.subplots(figsize=(10, 8))
fig.subplots_adjust(top=0.94,
                    bottom = 0.095,
                    left = 0.320,
                    right = 0.988,
                    hspace = 0.2,
                    wspace = 0.2)

# create a gradient colormap from red to green
colors = ['#FF0000', '#00FF00']
colors = list(reversed(colors))  # reverse the order of the colors
cmap = mcolors.LinearSegmentedColormap.from_list('color gradient', colors, len(df_top10))

# plot the horizontal bars with gradient colors
bars = ax.barh(df_top10['GameName'], df_top10['TotalMoney'], color=cmap(np.arange(len(df_top10))))

# set the plot title and labels
plt.title('Top 10 Games with the Highest Total Prize Money')
plt.xlabel('Total Money')
plt.ylabel('Game Name')

# set tick labels on x-axis to show values in millions
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{: .0f}M'.format(x/1000000)))

# show the plot
plt.show()


