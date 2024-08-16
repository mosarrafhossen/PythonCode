import re
# Specify the file name and the regular expression pattern
file_name = 'output.txt'
pattern = r'line\s+of'

# Open the file and search for the pattern
with open(file_name, 'r') as file:
    lines = file.readlines()

# Check each line for the pattern
for line_number, line in enumerate(lines, start=1):
    if re.search(pattern, line):
        print(f"Found pattern '{pattern}' in line {line_number}: {line.strip()}")
print("String search")
file_name = 'output1.txt'
search_term = 'line'

with open(file_name, 'r') as file:
    lines = file.readlines()

# for line_number, line in enumerate(lines, start=1):
#     if search_term in line:
#         print(f"Found '{search_term}' in line {line_number}: {line.strip()}")

    # Check each line for the search term
for line_number, line in enumerate(lines, start=1):
    if search_term in line:
        print(f"Found '{search_term}' in line {line_number}: {line.strip()}")
