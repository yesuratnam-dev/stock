import requests

x = requests.get('https://w3schools.com')
print(x.status_code)
print(x.headers.get('Content-Type') )



print(x.json)

print(str(x.content))