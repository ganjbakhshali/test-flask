import requests


# req= requests.get("http://127.0.0.1:5000/blog")
req= requests.post("http://127.0.0.1:5000/blog")
print(req.text)