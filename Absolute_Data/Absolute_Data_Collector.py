import json
import os
import requests

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to Filtered_Songs.json
filtered_songs_path = os.path.join(script_directory, '..', 'Data_Filter', 'Filtered_Songs.json')
token_info_file_path = os.path.join(script_directory, '..', 'User_Token', 'token_info.json')
# Now you can use filtered_songs_path in your code
print(filtered_songs_path)

# Spotify API endpoint for audio features
audio_features_url = 'https://api.spotify.com/v1/audio-features'

# Spotify API key (replace with your actual key)
with open(token_info_file_path, "r", encoding="utf-8") as token_file:
    token_file_data = json.load(token_file)
    spotify_api_key = token_file_data["access_token"]

with open(filtered_songs_path, "r", encoding="utf-8") as file:
    playlist_data = json.load(file)

# Maximum number of track URIs per request
max_tracks_per_request = 100

# Iterate through the playlist data in chunks of max_tracks_per_request
for i in range(0, len(playlist_data), max_tracks_per_request):
    # Extract track URIs for the current chunk
    chunk = playlist_data[i:i + max_tracks_per_request]

    # Filter out items without 'spotify_track_uri'
    chunk = [item for item in chunk if 'spotify_track_uri' in item]

    # Extract track URIs for the current chunk
    track_uris = [item['spotify_track_uri'].split(':')[-1] for item in chunk]
    print(track_uris)
    # Prepare the query parameters
    params = {'ids': ','.join(track_uris)}


    # Prepare the request headers
    headers = {'Authorization': f'Bearer {spotify_api_key}'}

    # Make the GET request to the Spotify API for audio features
    response = requests.get(audio_features_url, params=params, headers=headers)

    if response.status_code == 200:
        # Successful response
        audio_features_data = response.json()

        # Process the audio features data as needed
        for audio_features in audio_features_data['audio_features']:
            # Merge the audio features with the original playlist data
            # (you might want to customize this based on your needs)
            playlist_item = next(item for item in chunk if item['spotify_track_uri'].endswith(audio_features['id']))
            playlist_item.update(audio_features)

    else:
        # Error handling
        print(f"Error: {response.status_code}, {response.text}")

# Now, the playlist_data list contains the merged data