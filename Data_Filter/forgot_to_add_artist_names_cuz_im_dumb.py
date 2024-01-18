import os
import json

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory paths
initial_files_dir = os.path.join(current_dir, 'Stream_History_Files')
updated_files_dir = current_dir  # assuming 'updated_data.json' and 'updated_data_2.json' are in the same directory as the script
output_dir = os.path.join(current_dir, 'Output_Directory')

# Check if the output directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List to store artist data
artist_data_list = []

# Read artist data from initial files
for filename in os.listdir(initial_files_dir):
    if filename.endswith(".json"):
        file_path = os.path.join(initial_files_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            artist_data_list.extend(data)

# Rest of the code remains the same...


# Read and update data from updated files
updated_files = ['updated_data.json', 'updated_data_2.json']

for updated_file_name in updated_files:
    updated_file_path = os.path.join(updated_files_dir, updated_file_name)

    with open(updated_file_path, 'r', encoding='utf-8') as updated_file:
        updated_data = json.load(updated_file)

        for updated_entry in updated_data:
            uri_to_find = updated_entry['spotify_track_uri']

            # Find the corresponding entry in the artist_data_list
            matching_entry = next((entry for entry in artist_data_list if entry['spotify_track_uri'] == uri_to_find),
                                  None)

            if matching_entry:
                # Append artist data to the entry
                matching_entry.update(updated_entry)
            else:
                print(f"Entry with uri {uri_to_find} not found in the initial files.")

# Save the result to a new file
output_file_path = os.path.join(output_dir, 'result.json')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(artist_data_list, output_file, ensure_ascii=False, indent=2)

print(f"Result saved to {output_file_path}")
