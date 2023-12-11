import json

# Load the original JSON file
with open('Filtered_Songs.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Find the index where the first JSON object starts
start_index = 0
for index, line in enumerate(lines):
    if line.strip().startswith('{'):
        start_index = index
        break

# Calculate the midpoint index
midpoint = 47800 * 6  # Each JSON object has 6 lines

# Split the lines into two halves
first_half_lines = lines[:midpoint + start_index]
second_half_lines = lines[midpoint + start_index:]

# Save the two halves into separate files
with open('Filtered_Songs_Part_1.json', 'w', encoding='utf-8') as file:
    file.write("[\n")
    file.writelines(first_half_lines)
    file.write("]")

with open('Filtered_Songs_Part_2.Json', 'w', encoding='utf-8') as file:
    file.write("[\n")
    file.writelines(second_half_lines)
    file.write("]")
