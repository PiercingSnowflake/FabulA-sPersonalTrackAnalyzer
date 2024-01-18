import json

def fill_missing_values(data):
    filled_data = []

    for entry in data:
        # Check if the entry has missing values
        if any(entry.get(detail) is None for detail in ["danceability", "energy", "key", "loudness", "mode",
                                                         "speechiness", "acousticness", "instrumentalness",
                                                         "liveness", "valence", "tempo", "type", "id", "uri",
                                                         "track_href", "analysis_url", "duration_ms",
                                                         "time_signature"]):
            uri = entry.get("spotify_track_uri")

            if uri:
                # Find the matching entry with detailed values
                matching_entry = next((e for e in data if e["spotify_track_uri"] == uri and all(e.get(detail) is not None for detail in ["danceability", "energy", "key", "loudness", "mode",
                                                                                                                                     "speechiness", "acousticness", "instrumentalness",
                                                                                                                                     "liveness", "valence", "tempo", "type", "id", "uri",
                                                                                                                                     "track_href", "analysis_url", "duration_ms",
                                                                                                                                     "time_signature"])), None)

                if matching_entry:
                    # Update the missing values in the current entry
                    entry.update({k: v for k, v in matching_entry.items() if k not in entry})

        filled_data.append(entry)

    return filled_data

# Load your data from a file (adjust the filename as needed)
with open("result.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Call the function to fill missing values
filled_data = fill_missing_values(data)

# Now filled_data contains entries with additional details
# You can save this data to a new file or use it as needed
with open("result.json.json", 'w', encoding='utf-8') as output_file:
    json.dump(filled_data, output_file, ensure_ascii=False, indent=2)
