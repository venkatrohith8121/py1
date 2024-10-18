import json
# Example dictionary
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Serialize data to a file (dump)
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialize data from a file (load)
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)
