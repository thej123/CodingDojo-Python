# $ sudo pip install requests

import requests

r = requests.get('https://api.github.com/events')
r.text