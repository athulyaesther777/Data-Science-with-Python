import json

# Parsing JSON string to Python object
json_data = '{"name": "Alice", "age": 25}'
obj = json.loads(json_data)
print(obj['name'])  # Output: Alice

# Converting Python object to JSON string
json_string = json.dumps({"name": "Bob", "age": 30})
print(json_string)  # Output: '{"name": "Bob", "age": 30}'
