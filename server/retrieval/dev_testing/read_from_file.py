import json

# Define the path to your JSON file
file_path = "sources.json"  # Adjust the path if needed

# Open and load the JSON file
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)  # Read and parse JSON

sources = data.get('sources')
# Print the loaded data
print(len(sources))
print(sources[0])