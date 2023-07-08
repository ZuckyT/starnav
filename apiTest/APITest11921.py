import requests

response = requests.get('https://api.n2yo.com/rest/v1/satellite/positions/25544/41.7/-81.3/0/2&apiKey=QPFUCW-AESP2Q-2SUHA9-4SXG')
print(response.json())