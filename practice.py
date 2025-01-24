import requests
import json

payload = {"page":2}
x = requests.get('https://reqres.in//api/users',auth = ('username','password'))
jsonVar = x.json()

print(requests.codes.unauthorized)
print("bye")



