import json

def fill_missing_data(json_data, cache_file='uri_cache_2.json'):
    # Load the existing cache or create an empty one
    try:
        with open(cache_file, 'r', encoding='utf-8') as cache:
            uri_cache = json.load(cache)
    except (FileNotFoundError, json.JSONDecodeError):
        uri_cache = {}

    # Iterate through the JSON data
    for entry in json_data:
        # Check if the entry has detailed data
        if 'danceability' not in entry:
            # If not, check if the URI is in the cache
            uri = entry.get('spotify_track_uri', '')
            if uri in uri_cache:
                # If URI is in the cache, copy the missing data
                cached_data = uri_cache[uri]
                entry.update(cached_data)
            else:
                # If URI is not in the cache, find a matching entry
                matching_entry = next((e for e in json_data if e.get('spotify_track_uri', '') == uri and 'danceability' in e), None)
                if matching_entry:
                    # Update the cache with the found entry
                    uri_cache[uri] = {key: matching_entry[key] for key in matching_entry if key != 'spotify_track_uri'}
                    # Copy the missing data to the current entry
                    entry.update(uri_cache[uri])

    # Save the updated cache
    with open(cache_file, 'w', encoding='utf-8') as cache:
        json.dump(uri_cache, cache, ensure_ascii=False, indent=2)

# Load your JSON data
with open('Filtered_Songs_Part_2.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Call the function to fill missing data
fill_missing_data(json_data)

# Save the updated JSON data
with open('updated_data_2.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=2)
