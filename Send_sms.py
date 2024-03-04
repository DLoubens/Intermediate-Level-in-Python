import requests
from Location_phone import my_phone
resp = requests.post('https://textbelt.com/text', {
  'phone': my_phone,
  'message': 'Test message received, from Loubens D.',
  'key': 'textbelt',
})
print(resp.json())