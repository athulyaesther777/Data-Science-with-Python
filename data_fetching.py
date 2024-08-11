import requests

# Fetch data from an API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()
print(data)
