import requests

url = 'http://127.0.0.1:8000/edp'
payload = {
    "SQL": "CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY KEY)",
    "db": "test"
}

print('Sending request to', url)
resp = requests.post(url, json=payload)
print('Status code:', resp.status_code)
print('Response:', resp.json())
