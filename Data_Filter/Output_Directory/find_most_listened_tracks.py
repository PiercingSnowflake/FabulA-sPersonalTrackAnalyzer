import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the JSON file
with open("RealResult.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Group by track URI and calculate the total listening time in hours and play count
top_songs_hour = df.groupby('master_metadata_track_name')['ms_played'].sum().reset_index()
top_songs_hour['hours_played'] = top_songs_hour['ms_played'] / (1000 * 60 * 60)  # Convert milliseconds to hours
top_songs_count = df.groupby('master_metadata_track_name').size().reset_index(name='play_count')

# Sort the DataFrames by the corresponding metrics in descending order
top_songs_hour = top_songs_hour.sort_values(by='hours_played', ascending=False)
top_songs_count = top_songs_count.sort_values(by='play_count', ascending=False)

# Display the top 10 songs for hours played
print("Top 10 Most Listened Songs (Hours):")
print(top_songs_hour.head(10))
plt.figure(figsize=(12, 6))
sns.barplot(x='hours_played', y='master_metadata_track_name', data=top_songs_hour.head(10), palette='viridis', hue='master_metadata_track_name')
plt.title('Top 10 Most Listened Songs (Hours)')
plt.xlabel('Total Listening Time (Hours)')
plt.ylabel('Track Name')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Display the top 10 songs for play count
print("\nTop 10 Most Listened Songs (Play Count):")
print(top_songs_count.head(10))
plt.figure(figsize=(10, 6))
sns.barplot(x='play_count', y='master_metadata_track_name', data=top_songs_count.head(10), palette='viridis', hue='master_metadata_track_name')
plt.title('Top 10 Most Listened Songs (Play Count)')
plt.xlabel('Number of Plays')
plt.ylabel('Track Name')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
