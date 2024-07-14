import requests

url = "http://127.0.0.1:8000/memes"

data = {
    "url": "https://i.ytimg.com/vi/WeMsQPYPoVE/maxresdefault.jpg",
    "name": "amogus",
}

r = requests.post(url, params=data)

# r = requests.delete("http://127.0.0.1:8000/memes/12")

print(r.text)
#
# from sql import AdminDB
#
# user = AdminDB()
#
# create_admin = user.create_admin(username="innaro", password="12345678")