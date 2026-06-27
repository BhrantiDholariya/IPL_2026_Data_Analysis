import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IPL_2026.csv")
print(df.head())

#Basic Information
print(df.info())
print(df.shape)
print(df.isnull().sum())

#team won the most matches
match_wins = df['winner'].value_counts()
blue_gradient = sns.blend_palette(["#0B5394", "#7FB3D5"], n_colors=len(match_wins))
plt.figure(figsize=(10, 10))
sns.barplot(y = match_wins.index, x = match_wins.values, palette=blue_gradient)
plt.xlabel("Wins", fontsize=14)
plt.ylabel("Teams", fontsize=14)
plt.title("Most Match Wins by Team", fontsize=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.tight_layout()
plt.savefig("Most_Win.png")
plt.show()

#Toss decisions
sns.countplot(x = df['toss_decision'] , palette = ["#0B5394","#F26B38"])
plt.title("Toss_Decision")
plt.savefig("Toss_Decision.png")
plt.show()

#Toss Winner is the Match Winner
count = df[df['toss_winner'] == df['winner']]['date'].count()
percentage = (count * 100)/df.shape[0]
print(percentage)

#Team won by Wickets or Runs
win_by_runs = (df['win_by_runs'] > 0).sum()
win_by_wkts = (df['win_by_wickets'] > 0).sum()
comparison = {
    'Win_type' : ['Runs','Wickets'],
    'Count' : [win_by_runs,win_by_wkts]
}
pd.DataFrame(comparison)
sns.barplot(x = 'Win_type',y = 'Count',data = comparison , palette = ["#0B5394","#F26B38"])
plt.title('Wins by Runs vs Wins by Wickets')
plt.tight_layout()
plt.savefig("Win_by_Runs_vs_Wickets.png")
plt.show()

#Most POTM award
count = df['player_of_match'].value_counts().head(10)
print(count)
blue_gradient = sns.blend_palette(["#0B5394", "#7FB3D5"], n_colors=len(count))
sns.barplot(x=count.values, y=count.index, palette=blue_gradient)
plt.title("Top 10 Players with Most POTM Awards")
plt.tight_layout()
plt.savefig("Most_POTM_Awards.png")
plt.show()

#most match played by venue
venue_count = df['venue'].value_counts()    
print(venue_count)
short_labels = [
    'Narendra Modi Stadium',
    'Wankhede Stadium',
    'Ekana Stadium',
    'Eden Gardens',
    'MA Chidambaram Stadium',
    'Arun Jaitley Stadium',
    'Rajiv Gandhi Stadium',
    'Maharaja Yadavindra Stadium',
    'M Chinnaswamy Stadium',
    'Sawai Mansingh Stadium',
    'HPCA Stadium',
    'Barsapara Stadium',
    'Shaheed Veer Narayan Stadium'
]

def show_count(pct):
    total = sum(venue_count.values)
    count = round(pct * total / 100)
    return f'{count} matches'

plt.figure(figsize=(10, 10))
blue_gradient = sns.blend_palette(["#0B5394", "#7FB3D5"], n_colors=len(venue_count))
plt.pie(venue_count.values, labels=short_labels, autopct=show_count, colors=blue_gradient)
plt.title('Matches Played per Venue')
plt.tight_layout()
plt.savefig("Matches_Played_per_Venue.png")
plt.show()