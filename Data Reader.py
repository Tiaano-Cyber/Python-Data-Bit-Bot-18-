import json

# Step 1: Open the JSON file
with open('data.json', 'r') as file:
    # Step 2: Load the data from the JSON file
    data = json.load(file)

# Step 3: Print the data
print(data)
