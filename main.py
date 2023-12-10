from Data_Filter import Data_Filter


json_files = ['Streaming_History_Audio_2018-2019_0.json']  # Add more filenames as needed

# Keys to extract from each file
keys_to_extract = ['ms_played', 'master_metadata_track_name', 'skipped', 'spotify_track_uri']

# Dictionary to store extracted data
extracted_data_dict = {}

# Iterate through each JSON file
for file_path in json_files:
    extracted_data = extract_keys(file_path, keys_to_extract)
    extracted_data_dict[file_path] = extracted_data

# Print the extracted data
for file_path, data in extracted_data_dict.items():
    print(f"File: {file_path}, Extracted Data: {data}")
