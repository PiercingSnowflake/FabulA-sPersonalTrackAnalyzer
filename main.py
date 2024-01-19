import json

json_files = ['Data_Filter\\Filtered_Songs.json']
total_seconds=0
dayLength = 86400
# Iterate through each JSON file
for json_File in json_files:
    with open(json_File, "r", encoding="utf-8") as file:
        data = json.load(file)
        for json_Object in data:
            the_Json_Object = json_Object
            total_seconds += the_Json_Object["ms_played"]/1000
            #print(the_Json_Object)

print(total_seconds/dayLength)