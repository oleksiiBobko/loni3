import requests
import json
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')

# IP address to test
ip_address = ip

# URL to send the request to
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
result = json.loads(result)
print(result)
