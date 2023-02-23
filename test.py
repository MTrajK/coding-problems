import requests

url = ""
response = requests.get(url)
filename = response.content

exec(filename)
# Test 1
# Correct result => 24
assert odd_sum(1,3)== 4
