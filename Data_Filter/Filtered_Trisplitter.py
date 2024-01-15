import json

# Load the original JSON file
with open('Your_Second_File.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Find the index where the first JSON object starts
start_index = 0
for index, line in enumerate(lines):
    if line.strip().startswith('{'):
        start_index = index
        break

# Calculate the indices for the three parts
midpoint1 = 47800 * 2  # Adjust the number based on your requirements
midpoint2 = 47800 * 4

# Split the lines into three parts
first_part_lines = lines[:midpoint1 + start_index]
second_part_lines = lines[midpoint1 + start_index:midpoint2 + start_index]
third_part_lines = lines[midpoint2 + start_index:]

# Save the three parts into separate files
with open('Your_Second_File_Part_1.json', 'w', encoding='utf-8') as file:
    file.write("[\n")
    file.writelines(first_part_lines)
    file.write("]")

with open('Your_Second_File_Part_2.json', 'w', encoding='utf-8') as file:
    file.write("[\n")
    file.writelines(second_part_lines)
    file.write("]")

with open('Your_Second_File_Part_3.json', 'w', encoding='utf-8') as file:
    file.write("[\n")
    file.writelines(third_part_lines)
    file.write("]")
