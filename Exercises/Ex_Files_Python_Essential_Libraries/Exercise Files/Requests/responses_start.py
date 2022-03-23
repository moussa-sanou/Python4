# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# TODO: work with status codes
resp = requests.get("https://httpbin.org/status/200")
print(resp.status_code)
resp.raise_for_status()

# TODO: examine response encoding
resp = requests.get("https://httpbin.org/status/html")
print(resp.encoding)
print(resp.text)
print(resp.content)

# TODO: To read JSON content, use the json() function
resp = requests.get("https://httpbin.org/json")
print(resp.json())
print(resp.headers)
print(resp.headers['content-type'])