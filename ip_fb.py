import socket
import requests
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ip = s.getsockname()[0]

print(ip)

firebase_url = 'https://iotfb-fc0b9.firebaseio.com/'
data = {'ip':ip}
result = requests.put(firebase_url + '/raspberry.json', verify=False, data=json.dumps(data))
print(result)