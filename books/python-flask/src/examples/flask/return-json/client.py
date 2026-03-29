import requests

res = requests.get("http://localhost:5000/api/info")
print(res.status_code)
print(res.text)
print(type(res.text))
data = res.json()
print(type(data))
print(data)
print(data["hostname"])

