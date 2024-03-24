#!/usr/bin/python3

import urllib.request

# Define the URL to fetch
url = "https://alu-intranet.hbtn.io/status"

# Open the URL and fetch the response
with urllib.request.urlopen(url) as response:
    # Read the response body and decode it from bytes to UTF-8 string
    body = response.read().decode('utf-8')

# Print the content of the response body with tabulation
print("\t- type:", type(body))  # Print the type of the response body
print("\t- content:", body)     # Print the content of the response body
