import json

Json_File_List = ["Streaming_History_Audio_2018-2019_0.json",
                  "Streaming_History_Audio_2019_1.json",
                  "Streaming_History_Audio_2019-2020_2.json",
                  "Streaming_History_Audio_2020-2021_3.json",
                  "Streaming_History_Audio_2021-2022_4.json",
                  "Streaming_History_Audio_2022-2023_5.json",
                  "Streaming_History_Audio_2023_6.json",
                  "Streaming_History_Audio_2023_7.json"
                  ]

Keys_to_Extract = ["ms_played",
                   "master_metadata_track_name",
                   "spotify_track_uri"
                   ]

filtered_entries = []


for Json_File in Json_File_List:
    with open(Json_File, "r", encoding = "utf-8") as file:
        data = json.load(file)
        for json_object in data:
            if 'ms_played' in json_object and json_object['ms_played'] > 45000:

                Extracted_Data = {key: json_object[key] for key in Keys_to_Extract if key in json_object}
                filtered_entries.append(Extracted_Data)


with open("Filtered_Songs.json", "w", encoding="utf-8") as output_file:
    json.dump(filtered_entries, output_file, indent=2)

print(f"Filtered entries written to the file for you to use.")