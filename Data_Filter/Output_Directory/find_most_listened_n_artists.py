import pandas as pd
import json
import matplotlib.pyplot as plt

# Load the JSON data into a DataFrame
with open('RealResult.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

df = pd.DataFrame(data)

# Group by artist name and sum the total play time
artists_data = df.groupby('master_metadata_album_artist_name')['ms_played'].sum()

# Convert milliseconds to hours
artists_data_hours = artists_data / (1000 * 60 * 60)

# Sort the data to get the top 10 artists
top_artists = artists_data_hours.sort_values(ascending=False).head(10)

# Plotting
plt.figure(figsize=(10, 6))
top_artists.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Listened Artists')
plt.xlabel('Artist')
plt.ylabel('Total Play Time (Hours)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
