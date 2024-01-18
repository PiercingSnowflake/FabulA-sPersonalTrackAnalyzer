import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from JSON file
input_file_path = "RealResult.json"
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Convert timestamp to datetime format
df['ts'] = pd.to_datetime(df['ts'])

# Extract year and month from the timestamp
df['year'] = df['ts'].dt.year
df['month'] = df['ts'].dt.month

# Create a new column 'month_listened' with the month in a workable format
df['month_listened'] = df['ts'].dt.strftime('%Y-%m')

# Convert ms_played to numeric (assuming it's in milliseconds)
df['ms_played'] = pd.to_numeric(df['ms_played'], errors='coerce')

# Check for non-numeric values in the 'ms_played' column
non_numeric_mask = pd.to_numeric(df['ms_played'], errors='coerce').isna()
non_numeric_values = df.loc[non_numeric_mask, 'ms_played']

# Print non-numeric values
if not non_numeric_values.empty:
    print(f"Non-numeric values in 'ms_played': {non_numeric_values}")

# Replace non-numeric values with NaN
df.loc[non_numeric_mask, 'ms_played'] = pd.NA

# Group by month and calculate total listening time and number of songs played (converted to hours)
listening_time_per_month = df.groupby('month_listened')['ms_played'].sum() / (1000 * 60 * 60)
songs_played_per_month = df.groupby('month_listened').size()

# Set the color palette
sns.set_palette(['#669bbc'])

# Plotting total listening time over the months (bar chart)
plt.figure(figsize=(12, 6))
sns.barplot(x=listening_time_per_month.index, y=listening_time_per_month.values)
plt.title('Total Listening Time Over the Months')
plt.xlabel('Month Listened')
plt.ylabel('Total Listening Time (hours)')
plt.xticks(rotation=45)
plt.show()

# Set the color palette
sns.set_palette(['#669bbc'])

# Plotting number of songs played over the months (bar chart)
plt.figure(figsize=(12, 6))
sns.barplot(x=songs_played_per_month.index, y=songs_played_per_month.values)
plt.title('Number of Songs Played Over the Months')
plt.xlabel('Month Listened')
plt.ylabel('Number of Songs Played')
plt.xticks(rotation=45)
plt.show()
