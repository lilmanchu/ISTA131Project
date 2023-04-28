'''
Author: <Diego Colon>
Date: <4/24/23>
Class: ISTA 131
Section Leader: <Jacquie Kuru>
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Read in the data from the csv file
df = pd.read_csv('Final_CSV.csv', encoding='ISO-8859-1')

# Get the rows where the GameName is one of the specified games
games = ['Forza Motorsport 2', 'Forza Motorsport 3', 'Forza Motorsport 4', 'Forza Motorsport 6', 'Forza Motorsport 7']
df_games = df[df['GameName'].isin(games)]

# Create a dictionary to map each game to a unique color
color_dict = {game: plt.cm.tab10(i) for i, game in enumerate(games)}

# Create a scatter plot with one point for each game, colored and labeled by game
fig, ax = plt.subplots()
for game in games:
    color = color_dict[game]
    game_df = df_games[df_games['GameName'] == game]
    ax.scatter(game_df['Releaseyear'], game_df['TotalMoney'], color=color, label=game)
    for i, amount in enumerate(game_df['TotalMoney']):
        ax.annotate('${:,.0f}'.format(amount), (game_df.iloc[i]['Releaseyear'], amount))


# Add axis labels and a legend
ax.set_xlabel('Release Year')
ax.set_ylabel('Total Money Earned')
ax.legend()


# Add a line of regression
sns.regplot(data=df_games, x='Releaseyear', y='TotalMoney', scatter=False)

# Set the plot title
plt.title('Total Earnings of Forza Motorsport games in ESPORTS by Year')

# Show the plot
plt.tight_layout()
plt.show()
