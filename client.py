import requests

for i in range(10000):
    requests.post('http://127.0.0.1:8000/todo', {'content': str(i)})
