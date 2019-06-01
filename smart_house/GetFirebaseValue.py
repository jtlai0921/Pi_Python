import requests
import json

result = requests.get('https://iotfb-fc0b9.firebaseio.com/control.json')

if (json.loads(result.text)['light'] == 1):
    print('開燈')
else :
    print('關燈')

