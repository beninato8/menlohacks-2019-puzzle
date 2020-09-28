import requests
import json

postdata = {'body': "Go to bit.ly/menlohacksiv for a puzzle hint"}
url = 'https://api.menlohacks.com/admin/announcement'
headers = {'content-type': 'application/json', "X-MenloHacks-Authorization":'eyJhbGciOiJIUzI1NiIsImV4cCI6MTU1Mjg1NzI4MiwiaWF0IjoxNTUyMjUyNDgyfQ.eyJ1c2VybmFtZSI6InRob21hc0BtZW5sb2hhY2tzLmNvbSJ9.8FOl4wePHrqqOqdECHxHn6euMMYeS1icS9uyxOx2144'}
response = requests.post(url, data=postdata, headers=headers)
print(response)
print(response.content) 