# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# TODO: create a basic request for data
resp = requests.get("https://httpin.org/xml")
print(resp.status_code)
print(resp.text)

# TODO: create a request using parameters
args = {"key1": 1, "key2": "two", "key3": False}
resp = requests.get("https://httpin.org/get", params=args)
print(resp.text)
print(resp.url)

# TODO: create a request using POST
resp = requests.post("https://httpin.org/post", data={"key": "value"})
print(resp.text)

# TODO: create a request using custom headers
heads = {"my-custom-header": "this is a custom header"}
resp = requests.get("https://httpin.org/get", headers=heads)
print(resp.text)