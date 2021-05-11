from urllib.request import urlopen
import json

URL = 'https://api.thingspeak.com/channels/1385704/feeds.json?results=1'


with urlopen(URL) as url:
    data = json.loads(url.read().decode())
    print(data['feeds'][-1])
    print('Temp: ', data['feeds'][-1]['field1'])
    print('Hume: ', data['feeds'][-1]['field2'])
    print('Date: ', data['feeds'][-1]['created_at'].split('T')[0])
    print('Time: ', data['feeds'][-1]['created_at'].split('T')[1])
    # print(type(data))
